from typing import Optional

BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book():
    """Класс-конструктор экземпляра книги"""

    def __init__(self, id_: int, name: str, pages: int):
        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id_={self.id_}, name='{self.name}', pages={self.pages})"


class Library():
    """Класс-конструктор библиотеки, содержащий список книг"""
    next_book_id = 1
    def __init__(self, books: Optional = None):
        if not books:
            self.books = []
            self.book_id = Library.next_book_id
        else:
            self.books = books
            self.next_book_id = len(self.books) + 1

    def get_next_book_id(self)-> int:
        return self.next_book_id

    def get_index_by_book_id(self, book_id: int)-> int:
        id_name = enumerate(self.books, 0)
        for book in id_name:
            if book_id == book[1].id_:
                return book[1].id_
        else:
            raise ValueError("Книги с запрашиваемым id не существует")

    def __str__(self) -> str:
        return f'Библиотека {self.books}'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(books={self.books})'


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(3))  # проверяем индекс книги с id = 1
