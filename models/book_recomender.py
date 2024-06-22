from sklearn.neighbors import NearestNeighbors
from models.models import Book, UserBookOpinion
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
import numpy as np


def get_book_features(book):
    genre = book.genre if book.genre != 'N/A' else 'Unknown'
    author = book.author if book.author != 'N/A' else 'Unknown'
    try:
        year = int(book.publication_year)
    except (ValueError, TypeError):
        year = 0
    features = {
        'genre': genre,
        'author': author,
        'year': year
    }
    return features


def prepare_features(books, encoder=None):
    df = pd.DataFrame([get_book_features(book) for book in books])
    if encoder is None:
        encoder = OneHotEncoder(handle_unknown='ignore')
        encoded_features = encoder.fit_transform(df[['genre', 'author']]).toarray()
    else:
        encoded_features = encoder.transform(df[['genre', 'author']]).toarray()

    year_features = df[['year']].to_numpy()
    return np.hstack((encoded_features, year_features)), encoder


def recommend_books(user_id, n_recommendations=5):
    liked_books = UserBookOpinion.query.filter_by(user_id=user_id, likes=True).all()
    liked_books_ids = [opinion.book_id for opinion in liked_books]
    liked_books = Book.query.filter(Book.id.in_(liked_books_ids)).all()

    all_books = Book.query.all()
    all_books_ids = [book.id for book in all_books]

    all_books_features, encoder = prepare_features(all_books)
    liked_books_features, _ = prepare_features(liked_books, encoder=encoder)

    knn = NearestNeighbors(n_neighbors=n_recommendations, metric='cosine')
    knn.fit(all_books_features)

    distances, indices = knn.kneighbors(liked_books_features)

    recommended_books = []
    for idx in indices.flatten():
        book_id = all_books_ids[idx]
        if book_id not in liked_books_ids:
            recommended_books.append(Book.query.get(book_id))

    return recommended_books
