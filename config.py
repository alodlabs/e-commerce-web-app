import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "Pw-13-2040")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = os.getenv("FLASK_DEBUG", True)
