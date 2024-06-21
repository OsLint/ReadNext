import os

from flask import Flask, current_app
from flasgger import Swagger
from models.models import db, migrate, User, Book
from configurations import Config
import json


def create_app(config_class=Config):
    new_app = Flask(__name__)
    new_app.config.from_object(config_class)

    swagger = Swagger(new_app)

    db.init_app(new_app)
    migrate.init_app(new_app, db)

    with new_app.app_context():
        from controllers.app_controller import register_routes
        register_routes(new_app)

    return new_app


app = create_app()


@app.cli.command('seed_db')
def seed_db():
    print("[DEBUG] Seeding the database...")

    users = [
        {"name": "test1", "nickname": "test1", "password": "test1"},
        {"name": "test2", "nickname": "test2", "password": "test2"},
        {"name": "admin", "nickname": "admin", "password": "admin"},
    ]

    for user_data in users:
        if not User.query.filter_by(nickname=user_data["nickname"]).first():
            user = User(name=user_data["name"], nickname=user_data["nickname"], password=user_data["password"])
            db.session.add(user)
            print(f"[DEBUG] Adding user: {user_data['nickname']}")

    real_books_json_path = os.path.join(os.path.dirname(__file__), 'real_books.json')

    try:
        with open(real_books_json_path, 'r') as file:
            books_data = json.load(file)
    except FileNotFoundError:
        print("[ERROR] real_books.json file not found.")
        return
    except json.JSONDecodeError:
        print("[ERROR] Error decoding JSON from real_books.json.")
        return

    for book_data in books_data:
        if not Book.query.filter_by(title=book_data["title"]).first():
            book = Book(
                title=book_data["title"],
                author=book_data["author"],
                short_description=book_data["short_description"],
                genre=book_data["genre"],
                cover_photo_url=book_data["cover_photo_url"],
                publication_year=book_data["publication_year"]
            )
            db.session.add(book)
            print(f"[DEBUG] Adding book: {book_data['title']}")

    db.session.commit()
    print("[DEBUG] Database seeding completed.")


if __name__ == '__main__':
    app.run(debug=True)
