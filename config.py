import os

class Config:
    # Security
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key')  # Replace 'your-secret-key' with a secure, random string

    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///app.db')  # Default to SQLite for local development
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Avoids overhead of tracking changes in SQLAlchemy

    # Flask-SocketIO configuration
    SOCKETIO_MESSAGE_QUEUE = os.getenv('REDIS_URL', None)  # Optional: For production, use a Redis URL for scaling SocketIO

    # Additional settings
    DEBUG = os.getenv('FLASK_DEBUG', True)  # Enable or disable debug mode based on environment
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')  # Directory for storing uploaded files
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # Max upload size (16 MB)

