from app.repositories.book_repository import BookRepository

class BookService:

    @staticmethod
    def get_all_books(page=1, per_page=5):
        return BookRepository.get_all_books(page, per_page)
