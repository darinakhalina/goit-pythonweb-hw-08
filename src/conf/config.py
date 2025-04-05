import os

DB_HOST = os.getenv("DB_HOST", "localhost")


class Config:
    DB_URL = f"postgresql+asyncpg://postgres:1239@{DB_HOST}:5432/db-hw-8"


config = Config
