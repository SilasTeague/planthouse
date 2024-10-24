from flask import Flask
from flask_sqlalchemy import SQLAlchemy as sa
from flask_migrate import Migrate

# Initialize the database
db = sa()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///plants.db'  # Or use PostgreSQL URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize database and migration tool
    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        from . import app
    

    return app