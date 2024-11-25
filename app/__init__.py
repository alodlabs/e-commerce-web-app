from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO

db = SQLAlchemy()
socketio = SocketIO()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    socketio.init_app(app)

    with app.app_context():
        from .routes import main_bp
        app.register_blueprint(main_bp)

        # Create database tables
        db.create_all()

    return app
