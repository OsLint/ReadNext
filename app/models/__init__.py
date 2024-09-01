from .models import db, migrate,Book

def init_app(app):
    db.init_app(app)
    migrate.init_app(app, db)