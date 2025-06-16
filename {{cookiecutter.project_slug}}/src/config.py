import os

class Config:
    """Configuration settings for the application."""

    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
    SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///db.sqlite3")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

    # Add other configuration variables as needed

config = Config()