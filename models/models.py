from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    nickname = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    short_description = db.Column(db.String(1000), nullable=False)
    genre = db.Column(db.String(100), nullable=False)
    cover_photo_url = db.Column(db.String(1000), nullable=False)
    publication_year = db.Column(db.String(4), nullable=False)


class UserBookOpinion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    likes = db.Column(db.Boolean, nullable=False)
    review = db.Column(db.String(1000), nullable=True)


class UserBookRecommendation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    similar_books_liked_by_user = db.Column(db.Integer, nullable=False)
    similar_books_disliked_by_user = db.Column(db.Integer, nullable=False)
