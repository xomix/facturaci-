from fastapi import HTTPException
from passlib.context import CryptContext
from tortoise.exceptions import DoesNotExist, IntegrityError

from src.database.models import Users
from src.schemas.users import UserOutSchema, UserInSchema


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def create_user(user: UserInSchema) -> UserOutSchema:
    user.password = pwd_context.encrypt(user.password)

    try:
        user_obj = await Users.create(**user.model_dump(exclude_unset=True))
    except IntegrityError as e:
        raise HTTPException(status_code=401, detail="Sorry, that username already exists.") from e

    return await UserOutSchema.from_tortoise_orm(user_obj)


async def delete_user(user_id: int, current_user: UserInSchema) -> str:
    try:
        db_user = await UserOutSchema.from_queryset_single(Users.get(id=user_id))
    except DoesNotExist as e:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found") from e

    if db_user.id == current_user.id: # TODO: Verify we have the correct role instead
        deleted_count = await Users.filter(id=user_id).delete()
        if not deleted_count:
            raise HTTPException(status_code=404, detail=f"User {user_id} not found")
        return f"Deleted user {user_id}"

    raise HTTPException(status_code=403, detail="Not authorized to delete")
