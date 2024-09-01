from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

class Book(db.Model):
    """
    Book model for storing book related
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    short_description = db.Column(db.String(1000), nullable=False)
    genre = db.Column(db.String(100), nullable=False)
    cover_photo_url = db.Column(db.String(1000), nullable=False)
    publication_year = db.Column(db.String(4), nullable=False)
    likes = db.Column(db.Integer, default=0)

    def to_dict(self):
        """
        Convert the SQLAlchemy model instance into a dictionary.
        """
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'short_description': self.short_description,
            'genre': self.genre,
            'cover_photo_url': self.cover_photo_url,
            'publication_year': self.publication_year,
            'likes': self.likes
        }
