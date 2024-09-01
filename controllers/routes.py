from flask import request, jsonify
from flask_login import LoginManager, current_user, login_required, logout_user

from services.user_service import UserService
from services.book_service import BookService

login_manager = LoginManager()


def register_routes(app):
    login_manager.init_app(app)

    @app.route('/api/books?page=<int:page>', methods=['GET'])
    def get_books():
        page = request.args.get('page', type=int)
        title = request.args.get('title', '')
        author = request.args.get('author', '')
        year = request.args.get('year', type=int)
        genre = request.args.get('genre', '')

        books = BookService.search_books(title, author, year, genre, page=page, per_page=20, current_user=current_user)
        response = jsonify({'books': [book.to_dict() for book in books]})
        return response


    @app.route('/api/login', methods=['POST'])
    def login():
        nickname = request.form.get('nickname')
        password = request.form.get('password')
        logged_in = UserService.login(nickname, password)
        if logged_in:
            return jsonify({'message': 'Login successful', 'status': 'success'})
        else:
            return jsonify({'message': 'Invalid credentials', 'status': 'failure'}), 400

    @app.route('/api/logout')
    @login_required
    def logout():
        logout_user()
        return jsonify({'message': 'Logout successful', 'status': 'success'}), 200

    @app.route('/api/register', methods=['POST'])
    def register():
        name = request.form.get('name')
        nickname = request.form.get('nickname')
        password = request.form.get('password')

        registered = UserService.register(name, nickname, password)
        if registered:
            return jsonify({'message': 'Registration successful', 'status': 'success'})
        else:
            return jsonify({'message': 'User already exists', 'status': 'failure'}), 400
