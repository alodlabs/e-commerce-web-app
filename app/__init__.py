from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO

# Initialize extensions
db = SQLAlchemy()
socketio = SocketIO()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Initialize Flask extensions
    db.init_app(app)
    socketio.init_app(app)

    # Register blueprints
    with app.app_context():
        from .routes import main_bp
        app.register_blueprint(main_bp)

        # Create database tables if they don't exist
        db.create_all()

        # WebSocket event handlers
        @socketio.on('message')
        def handle_message(msg):
            print(f"Message received: {msg}")
            # Broadcast the message to all connected clients
            socketio.emit('message', msg, broadcast=True)

    return app
