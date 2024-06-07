from flask import Flask, request, jsonify, render_template
from models import db, User, Book, UserPreference
from config import Config
from recomendation import recommend_books

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    new_user = User(username=data['username'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User added successfully'}), 201


@app.route('/add_book', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = Book(title=data['title'])
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'message': 'Book added successfully'}), 201


@app.route('/add_preference', methods=['POST'])
def add_preference():
    data = request.get_json()
    new_pref = UserPreference(user_id=data['user_id'], book_id=data['book_id'], rating=data['rating'])
    db.session.add(new_pref)
    db.session.commit()
    return jsonify({'message': 'Preference added successfully'}), 201


@app.route('/recommend/<int:user_id>', methods=['GET'])
def recommend(user_id):
    recommendations = recommend_books(user_id)
    return jsonify(recommendations), 200


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
