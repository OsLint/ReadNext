import os


class Config:
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'book_recommendation.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
