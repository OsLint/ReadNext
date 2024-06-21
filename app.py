from flask import Flask, request, render_template, jsonify
from flasgger import Swagger, swag_from
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)
swagger = Swagger(app)

# Configuration for SQL Server
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://sa:xaxaxa1234@localhost/master?driver=ODBC+Driver+17+for+SQL+Server'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    nickname = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
@swag_from({
    'responses': {
        200: {
            'description': 'Login successful',
            'examples': {
                'application/json': {
                    'message': 'Login successful',
                    'status': 'success'
                }
            }
        },
        400: {
            'description': 'Invalid credentials',
            'examples': {
                'application/json': {
                    'message': 'Invalid credentials',
                    'status': 'failure'
                }
            }
        }
    },
    'parameters': [
        {
            'name': 'nickname',
            'in': 'formData',
            'type': 'string',
            'required': True,
            'description': 'User Nickname'
        },
        {
            'name': 'password',
            'in': 'formData',
            'type': 'string',
            'required': True,
            'description': 'User password'
        }
    ]
})
def login():
    nickname = request.form.get('nickname')
    password = request.form.get('password')

    user = User.query.filter_by(nickname=nickname, password=password).first()

    if user:
        print(f"[DEBUG] Login successful for user: {nickname}")
        return jsonify({'message': 'Login successful', 'status': 'success'})
    else:
        print(f"[DEBUG] Invalid login attempt for user: {nickname}")
        return jsonify({'message': 'Invalid credentials', 'status': 'failure'}), 400


@app.route('/register', methods=['POST'])
@swag_from({
    'responses': {
        200: {
            'description': 'Registration successful',
            'examples': {
                'application/json': {
                    'message': 'Registration successful',
                    'status': 'success'
                }
            }
        }
    },
    'parameters': [
        {
            'name': 'name',
            'in': 'formData',
            'type': 'string',
            'required': True,
            'description': 'User name'
        },
        {
            'name': 'nickname',
            'in': 'formData',
            'type': 'string',
            'required': True,
            'description': 'User Nickname'
        },
        {
            'name': 'password',
            'in': 'formData',
            'type': 'string',
            'required': True,
            'description': 'User password'
        }
    ]
})
def register():
    name = request.form.get('name')
    nickname = request.form.get('nickname')
    password = request.form.get('password')

    if User.query.filter_by(nickname=nickname).first():
        print(f"[DEBUG] Registration failed: User {nickname} already exists.")
        return jsonify({'message': 'User already exists', 'status': 'failure'}), 400

    new_user = User(name=name, nickname=nickname, password=password)
    db.session.add(new_user)
    db.session.commit()
    print(f"[DEBUG] User registered: {nickname}")

    return jsonify({'message': 'Registration successful', 'status': 'success'})


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
