from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
# Initialize extensions globally
db = SQLAlchemy()
bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

    # Initialize extensions with the app
    db.init_app(app)
    bcrypt.init_app(app)

    # Import and register blueprints here
    from flaskblog.routes import main
    app.register_blueprint(main)

    return app
login_manager = LoginManager(create_app)