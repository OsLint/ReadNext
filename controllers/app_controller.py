from flask import request, render_template, jsonify, redirect, url_for
from flasgger import swag_from
from flask_login import LoginManager, current_user, login_required, logout_user

from models.models import User, UserBookOpinion
from services.user_service import UserService
from services.book_service import BookService

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
        logged_in = UserService.login(nickname, password)

        if logged_in:
            return redirect(url_for('home'))
        else:
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

        registered = UserService.register(name, nickname, password)
        if registered:
            return redirect(url_for('home'))
        else:
            return jsonify({'message': 'User already exists', 'status': 'failure'}), 400

    @app.route('/home')
    @login_required
    def home():
        page = request.args.get('page', 1, type=int)
        title = request.args.get('title', '')
        author = request.args.get('author', '')
        year = request.args.get('year', type=int)
        genre = request.args.get('genre', '')

        books = BookService.search_books(title, author, year, genre, page=page, per_page=5, current_user=current_user)
        return render_template('home.html', user=current_user, books=books, page=page)

    @app.route('/profile')
    @login_required
    def profile():
        page = request.args.get('page', 1, type=int)
        title = request.args.get('title', '')
        author = request.args.get('author', '')
        year = request.args.get('year', type=int)
        genre = request.args.get('genre', '')

        books = BookService.search_liked_books(title, author, year, genre, page=page, per_page=5,
                                               user_id=current_user.id)
        return render_template('profile.html', user=current_user, books=books, page=page, per_page=5)

    @app.route('/like_book', methods=['POST'])
    @login_required
    def like_book():
        data = request.get_json()
        book_id = data.get('book_id')
        if book_id:
            likes = BookService.like_book(book_id, current_user.id)
            return jsonify({'likes': likes, 'isLiked': True})
        return jsonify({'message': 'Book ID not provided'}), 400

    @app.route('/dislike_book', methods=['POST'])
    @login_required
    def dislike_book():
        data = request.get_json()
        book_id = data.get('book_id')
        if book_id:
            likes = BookService.dislike_book(book_id, current_user.id)
            return jsonify({'likes': likes, 'isLiked': False})
        return jsonify({'message': 'Book ID not provided'}), 400

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        return redirect(url_for('index'))

    @app.route('/recommendations')
    @login_required
    def recommendations():
        page = request.args.get('page', 1, type=int)
        liked_books = UserBookOpinion.query.filter_by(user_id=current_user.id, likes=True).all()

        if len(liked_books) < 5:
            message = ("You need to like at least 5 books to get recommendations. Please like more books before you "
                       "get back here.")
            books = BookService.get_all_books(page=page, per_page=5, current_user=current_user)
            return render_template('recommendations.html', user=current_user, books=books, message=message, page=page)

        recommended_books = BookService.get_book_recommendations(current_user.id)
        return render_template('recommendations.html', user=current_user, books=recommended_books, page=page)
