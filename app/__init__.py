from flask import Flask
from .extensions import db, login_manager, csrf
from .config import Config
from .models import User


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # Load configuration
    app.config.from_object(Config)
    app.config.from_pyfile("config.py", silent=True)

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)

    # User loader for Flask-Login
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register blueprints
    from .routes import main
    app.register_blueprint(main)

    return app
