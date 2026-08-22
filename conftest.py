
import pytest
from main import BooksCollector


@pytest.fixture
def books_collection():
    return BooksCollector()


@pytest.fixture
def my_books_collection():
    collection = BooksCollector()
    books = ['Симбиоз', 'Демон', 'Внутри убийцы', 'Гадкий Я', 'Ревизор']
    genres = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

    for title, genre in zip(books, genres):
        collection.add_new_book(title)
        collection.set_book_genre(title, genre)

    return collection