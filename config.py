import os
from pathlib import Path


class Config:
    """Set Flask configuration vars."""

    # General Config
    FLASK_APP = os.environ.get("FLASK_APP") or "movieuplink"
    SECRET_KEY = os.environ.get("SECRET_KEY") or "secret_key"

    ENV = os.environ.get("FLASK_ENV") or "development"
    if ENV == "development":
        DEBUG = True

    # Instance folder and cache
    INSTANCE_PATH = os.environ.get("INSTANCE_PATH") or Path.cwd() / "instance"
    INSTANCE_PATH.mkdir(exist_ok=True)

    CACHEDB_NAME = os.environ.get("CACHE_NAME") or INSTANCE_PATH / FLASK_APP

    # TMDB API
    API_KEY = os.environ.get("API_KEY") or "Your TMDB API key needs to be set!"


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
