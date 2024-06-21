from flask import request, render_template, jsonify
from flasgger import swag_from
from flask_login import LoginManager, login_user, current_user, login_required
from models.models import User
from repositories.user_repository import UserRepository

login_manager = LoginManager()


def register_routes(app):
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

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

        user = UserRepository.get_by_nickname_and_password(nickname, password)

        if user:
            login_user(user)
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

        if UserRepository.get_by_nickname(nickname):
            print(f"[DEBUG] Registration failed: User {nickname} already exists.")
            return jsonify({'message': 'User already exists', 'status': 'failure'}), 400

        UserRepository.add_user(name, nickname, password)
        print(f"[DEBUG] User registered: {nickname}")

        return jsonify({'message': 'Registration successful', 'status': 'success'})

    @app.route('/profile')
    @login_required
    def profile():
        return render_template('profile.html', user=current_user)
