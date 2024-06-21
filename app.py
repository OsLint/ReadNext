from flask import Flask
from flasgger import Swagger
from models.models import db, migrate
from models.configurations import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    swagger = Swagger(app)

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        from controllers.app_controller import register_routes
        register_routes(app)

    return app


app = create_app()


# Seed command to add initial data to the database
@app.cli.command('seed_db')
def seed_db():
    """Seed the database with initial data."""
    print("[DEBUG] Seeding the database...")
    users = [
        {"name": "John Doe", "nickname": "john", "password": "john123"},
        {"name": "Jane Smith", "nickname": "jane", "password": "jane123"},
        {"name": "Alice Johnson", "nickname": "alice", "password": "alice123"},
    ]

    for user_data in users:
        if not User.query.filter_by(nickname=user_data["nickname"]).first():
            user = User(name=user_data["name"], nickname=user_data["nickname"], password=user_data["password"])
            db.session.add(user)
            print(f"[DEBUG] Adding user: {user_data['nickname']}")
    db.session.commit()
    print("[DEBUG] Database seeding completed.")


if __name__ == '__main__':
    app.run(debug=True)
