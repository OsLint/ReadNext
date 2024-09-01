from flask import jsonify

from app.services import BookService


def register_routes(app):
    @app.route('/api/books', methods=['GET'])
    def get_books():
        """
                Get a list of books
                ---
                tags:
                  - Books
                parameters:
                  - name: page
                    in: query
                    type: integer
                    required: false
                    default: 1
                    description: The page number to retrieve.
                  - name: per_page
                    in: query
                    type: integer
                    required: false
                    default: 20
                    description: Number of books to retrieve per page.
                responses:
                  200:
                    description: A list of books
                    schema:
                      type: object
                      properties:
                        books:
                          type: array
                          items:
                            type: object
                            properties:
                              id:
                                type: integer
                                description: The book ID
                                example: 1
                              title:
                                type: string
                                description: The book title
                                example: "The Great Gatsby"
                              author:
                                type: string
                                description: The book author
                                example: "F. Scott Fitzgerald"
                              short_description:
                                type: string
                                description: A short description of the book
                                example: "A novel set in the Roaring Twenties."
                              genre:
                                type: string
                                description: The genre of the book
                                example: "Fiction"
                              cover_photo_url:
                                type: string
                                description: URL of the book's cover photo
                                example: "http://example.com/cover.jpg"
                              publication_year:
                                type: string
                                description: The year the book was published
                                example: "1925"
                              likes:
                                type: integer
                                description: The number of likes the book has received
                                example: 250
                """
        books = BookService.get_all_books(page=1, per_page=20)
        response = jsonify({'books': [book.to_dict() for book in books]})
        return response
