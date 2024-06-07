from models import UserPreference, Book
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sklearn.neighbors import NearestNeighbors
import pandas as pd

engine = create_engine('postgresql://username:password@localhost:5432/book_recommendation_db')
Session = sessionmaker(bind=engine)
session = Session()


def recommend_books(user_id):
    preferences = session.query(UserPreference).all()
    data = [(p.user_id, p.book_id, p.rating) for p in preferences]
    df = pd.DataFrame(data, columns=['user_id', 'book_id', 'rating'])

    user_book_matrix = df.pivot(index='user_id', columns='book_id', values='rating').fillna(0)
    knn = NearestNeighbors(metric='cosine', algorithm='brute')
    knn.fit(user_book_matrix)

    user_index = list(user_book_matrix.index).index(user_id)
    distances, indices = knn.kneighbors(user_book_matrix.iloc[user_index, :].values.reshape(1, -1), n_neighbors=6)

    recommended_books = []
    for i in range(1, len(distances.flatten())):
        book_indices = user_book_matrix.columns[indices.flatten()[i]]
        recommended_books.extend([session.query(Book).get(b).title for b in book_indices])

    return recommended_books
