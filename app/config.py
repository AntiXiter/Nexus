from __future__ import annotations
import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "instance/uploads")
    MAX_CONTENT_LENGTH = int(os.getenv("MAX_CONTENT_LENGTH", 50 * 1024 * 1024))

    # cache / rate-limit
    CACHE_TYPE = "SimpleCache"
    RATELIMIT_DEFAULT = "200/hour"

def carregar_config(nome: str | None = None) -> type[Config]:
    return Config
