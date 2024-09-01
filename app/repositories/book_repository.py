from book_recomendation_service import recommend_books
from models import Book, UserBookOpinion, db


class BookRepository:

    @staticmethod
    def get_all_books(page=1, per_page=20, current_user=None):
        paginated_query = Book.query.order_by(Book.title.asc()).paginate(page=page, per_page=per_page, error_out=False)
        books = paginated_query.items
        if current_user:
            user_likes = {like.book_id for like in UserBookOpinion.query.filter_by(user_id=current_user.id).all()}
            for book in books:
                book.liked_by_user = book.id in user_likes
        return books


    @staticmethod
    def get_by_id(book_id):
        return Book.query.get(book_id)

    @staticmethod
    def get_by_title(title):
        return Book.query.filter_by(title=title).first()

    @staticmethod
    def like_book(book_id, user_id):
        book = Book.query.get(book_id)
        if not book:
            return None

        existing_opinion = UserBookOpinion.query.filter_by(user_id=user_id, book_id=book_id, likes=True).first()
        if existing_opinion:
            return book.likes

        book.likes += 1
        opinion = UserBookOpinion(user_id=user_id, book_id=book_id, likes=True)
        db.session.add(opinion)
        db.session.commit()
        return book.likes

    @staticmethod
    def dislike_book(book_id, user_id):
        book = Book.query.get(book_id)
        if not book:
            return None

        existing_opinion = UserBookOpinion.query.filter_by(user_id=user_id, book_id=book_id, likes=True).first()
        if not existing_opinion:
            return book.likes

        book.likes -= 1
        db.session.delete(existing_opinion)
        db.session.commit()
        return book.likes

    @staticmethod
    def add_user_book_opinion(book, current_user, likes=True):
        user_book_opinion = UserBookOpinion(user_id=current_user.id, book_id=book.id, likes=likes)
        db.session.add(user_book_opinion)
        db.session.commit()
        return user_book_opinion

    @staticmethod
    def search_books(title='', author='', year=None, genre='', page=1, per_page=5, current_user=None):
        query = Book.query
        if title:
            query = query.filter(Book.title.ilike(f'%{title}%'))
        if author:
            query = query.filter(Book.author.ilike(f'%{author}%'))
        if year:
            query = query.filter(Book.publication_year == year)
        if genre:
            query = query.filter(Book.genre.ilike(f'%{genre}%'))
        query = query.order_by(Book.title.asc())

        paginated_query = query.paginate(page=page, per_page=per_page, error_out=False)
        books = paginated_query.items
        if current_user:
            user_likes = {like.book_id for like in UserBookOpinion.query.filter_by(user_id=current_user.id).all()}
            for book in books:
                book.liked_by_user = book.id in user_likes
        return books

    @staticmethod
    def search_liked_books(title='', author='', year=None, genre='', page=1, per_page=5, user_id=None):
        query = Book.query.join(UserBookOpinion).filter(UserBookOpinion.user_id == user_id,
                                                        UserBookOpinion.likes == True)
        if title:
            query = query.filter(Book.title.ilike(f'%{title}%'))
        if author:
            query = query.filter(Book.author.ilike(f'%{author}%'))
        if year:
            query = query.filter(Book.publication_year == year)
        if genre:
            query = query.filter(Book.genre.ilike(f'%{genre}%'))
        query = query.order_by(Book.title.asc())

        paginated_query = query.paginate(page=page, per_page=per_page, error_out=False)
        books = paginated_query.items
        for book in books:
            book.liked_by_user = True
        return books

    @staticmethod
    def get_book_recommendations(user_id):
        return recommend_books(user_id)
