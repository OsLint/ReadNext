from flask import request, render_template, jsonify
from flasgger import swag_from
from models.models import User, db


def register_routes(app):
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
