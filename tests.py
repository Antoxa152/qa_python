import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_rating()) == 2

    def test_add_new_book_already_added_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        collector.add_new_book('Гордость и предубеждение')
        assert collector.get_books_genre() == {'Гордость и предубеждение': ''}


    @pytest.mark.parametrize('name', ['',
                                      'Удивительное путешествие Нильса Хольгерсс',
                                      'Удивительное путешествие Нильса Хольгерссона с дикими гусями по Швеции'])
    def test_add_new_book_name_out_of_range(self, name, books_collection):
        books_collection.add_new_book(name)
        assert len(books_collection.get_books_genre()) == 0


    @pytest.mark.parametrize('name', ['К югу от границы',
                                      'Любовь как роза, красива, но шипы больны',
                                      'Я'])
    def test_add_new_book_name_in_the_range(self, name, books_collection):
        books_collection.add_new_book(name)
        assert name in books_collection.get_books_genre()


    def test_set_book_genre_to_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_genre('Гордость и предубеждение', 'Фантастика')
        assert collector.get_books_genre() == {'Гордость и предубеждение': 'Фантастика'}


    def test_set_book_genre_to_not_existing_book(self):
        collector = BooksCollector()
        collector.set_book_genre('Гордость и предубеждение', 'Фантастика')
        assert collector.get_books_genre() == {}


    def test_set_book_genre_to_not_existing_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_genre('Гордость и предубеждение', 'Трагикомедии')
        assert collector.get_books_genre() == {'Гордость и предубеждение': ''}


    @pytest.mark.parametrize('name, genre', [('Гордость и предубеждение и зомби', 'Ужасы'),
                                             ('Что делать, если ваш кот хочет вас убить', 'Комедии')])
    def test_get_book_genre_by_name(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre


    @pytest.mark.parametrize('name, genre', [('Гордость и предубеждение и зомби', 'Ужасы'),
                                             ('Что делать, если ваш кот хочет вас убить', 'Комедии')])
    def test_get_books_with_specific_genre_by_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_books_with_specific_genre(genre) == [name]


    def test_get_books_with_specific_genre_by_wrong_genre(self, my_books_collection):
        assert len(my_books_collection.get_books_with_specific_genre('Трагикомедии')) == 0


    def test_get_books_for_children(self, my_books_collection):
        assert len(my_books_collection.get_books_for_children()) == 3 and my_books_collection.get_books_for_children() == ['Симбиоз', 'Гадкий Я', 'Ревизор']


    def test_add_book_in_favorites_not_added_in_favorites_book(self, my_books_collection):
        my_books_collection.add_book_in_favorites('Симбиоз')
        assert 'Симбиоз' in my_books_collection.get_list_of_favorites_books() and len(my_books_collection.get_list_of_favorites_books()) == 1


    def test_add_book_in_favorites_added_in_favorites_book(self, my_books_collection):
        my_books_collection.add_book_in_favorites('Симбиоз')
        my_books_collection.add_book_in_favorites('Симбиоз')
        assert 'Симбиоз' in my_books_collection.get_list_of_favorites_books() and len(my_books_collection.get_list_of_favorites_books()) == 1


    def test_add_book_in_favorites_not_added_dict_book(self, my_books_collection):
        book = 'Идиот'
        my_books_collection.add_book_in_favorites(book)
        assert len(my_books_collection.get_list_of_favorites_books()) == 0


    def test_delete_book_from_favorites(self, my_books_collection):
        my_books_collection.add_book_in_favorites('Симбиоз')
        my_books_collection.delete_book_from_favorites('Симбиоз')
        assert len(my_books_collection.get_list_of_favorites_books()) == 0


    def test_delete_book_from_favorites_deleted_book(self, my_books_collection):
        my_books_collection.add_book_in_favorites('Симбиоз')
        my_books_collection.delete_book_from_favorites('Гадкий Я')
        assert len(my_books_collection.get_list_of_favorites_books()) == 1 and 'Гадкий Я' not in my_books_collection.get_list_of_favorites_books()


    def test_get_list_of_favorites_books(self, my_books_collection):
        my_books_collection.add_book_in_favorites('Симбиоз')
        my_books_collection.add_book_in_favorites('Гадкий Я')
        assert my_books_collection.get_list_of_favorites_books() == ['Симбиоз', 'Гадкий Я']

