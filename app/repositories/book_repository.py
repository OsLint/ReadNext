from app.models import Book



class BookRepository:
    @staticmethod
    def get_all_books(page=1, per_page=20):
        paginated_query = Book.query.order_by(Book.title.asc()).paginate(page=page, per_page=per_page, error_out=False)
        books = paginated_query.items
        return books


