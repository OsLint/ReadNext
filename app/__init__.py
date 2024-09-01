import os
import json
from random import Random
from flask import Flask
from flasgger import Swagger
from flask_cors import CORS
from .config import Config
from .models import db, migrate, Book
from app.api.routes import register_routes

from .models.models import Book, db


def create_app(config_class=Config):
    """
    Create a Flask application using the app factory pattern.
    :param config_class:
    :return: app
    """
    """
    :param config_class: 
    :return: 
    """
    app = Flask(__name__)
    app.config.from_object(config_class)

    # initialize extensions
    CORS(app, resources={r"/api/*": {"origins": "http://localhost:4200"}})
    Swagger(app)
    init_db(app)  # Initialize the database

    with app.app_context():
        register_routes(app)
        register_cli_commands(app)

    return app


def init_db(app):
    """
    Initialize the database.
    :param app:Flask
    :return:
    """
    db.init_app(app)
    migrate.init_app(app, db)


def register_cli_commands(app):
    """
    Register CLI commands.
    :param app:
    :return:
    """
    @app.cli.command('seed_db')
    def seed_db():
        print("[DEBUG] Seeding the database...")
        real_books_json_path = os.path.join(os.path.dirname(__file__), './instance/books.json')
        try:
            with open(real_books_json_path, 'r') as file:
                books_data = json.load(file)
        except FileNotFoundError:
            print("[ERROR] books.json file not found.")
            return
        except json.JSONDecodeError:
            print("[ERROR] Error decoding JSON from books.json.")
            return

        for book_data in books_data:
            if not Book.query.filter_by(title=book_data["title"]).first():
                book = Book(
                    title=book_data["title"],
                    author=book_data["author"],
                    short_description=book_data["short_description"],
                    genre=book_data["genre"],
                    cover_photo_url=book_data["cover_photo_url"],
                    publication_year=book_data["publication_year"],
                    likes=Random().randint(0, 1999)
                )
                db.session.add(book)
                print(f"[DEBUG] Adding book: {book_data['title']}")

        db.session.commit()
        print("[DEBUG] Database seeding completed.")
