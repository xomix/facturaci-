import os

DATABASE_URL = 'sqlite://db.sqlite3'

TORTOISE_ORM = {
    #"connections": {"default": os.environ.get("DATABASE_URL")},
    "connections": {"default": DATABASE_URL},
    "apps": {
        "models": {
            "models": [
                "src.database.models", "aerich.models"
            ],
            "default_connection": "default"
        }
    }
}