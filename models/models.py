from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


class DatabaseContext:
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        db.init_app(app)
        migrate.init_app(app, db)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    nickname = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    liked_books = db.relationship('Book', secondary='user_book_opinion', backref='liked_by')


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    short_description = db.Column(db.String(1000), nullable=False)
    genre = db.Column(db.String(100), nullable=False)
    cover_photo_url = db.Column(db.String(1000), nullable=False)
    publication_year = db.Column(db.String(4), nullable=False)
    likes = db.Column(db.Integer, default=0)


class UserBookOpinion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    likes = db.Column(db.Boolean, nullable=False)


class UserBookRecommendation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    similar_books_liked_by_user = db.Column(db.Integer, nullable=False)
    similar_books_disliked_by_user = db.Column(db.Integer, nullable=False)
