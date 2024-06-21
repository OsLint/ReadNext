from repositories.book_repository import BookRepository


class BookService:

    @staticmethod
    def get_all_books(page=1, per_page=5, current_user=None):
        return BookRepository.get_all_books(page, per_page, current_user)

    @classmethod
    def like_book(cls, book_id, user_id):
        return BookRepository.like_book(book_id, user_id)

    @classmethod
    def dislike_book(cls, book_id, user_id):
        return BookRepository.dislike_book(book_id, user_id)

    @staticmethod
    def search_books(title='', author='', year=None, genre='', page=1, per_page=5, current_user=None):
        return BookRepository.search_books(title, author, year, genre, page, per_page, current_user)
