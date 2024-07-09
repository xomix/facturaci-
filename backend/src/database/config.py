import os

connexion = "sqlite://example.db"
if "DATABASE_URL" in os.environ:
    connexion = os.environ.get("DATABASE_URL")

TORTOISE_ORM = {
    "connections": {"default": connexion},
    "apps": {
        "models": {
            "models": [
                "src.database.models", "aerich.models"
            ],
            "default_connection": "default"
        }
    }
}