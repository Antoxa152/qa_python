test_add_new_book_add_two_books: проверка добавления двух книг
test_add_new_book_already_added_book: негативная проверка на повторное добавление книги
test_add_new_book_name_out_of_range: негативная проверка на добавление книги с невалидным названием
test_add_new_book_name_in_the_range: проверка на добавление книги с валидным названием
test_set_book_genre_to_existing_book: проверка на добавление жанра из genre для книги из books_genre
test_set_book_genre_to_not_existing_book: негативная проверка на добавление жанра из genre для книги не из books_genre
test_set_book_genre_to_not_existing_genre: негативная проверка на добавление жанра НЕ из genre для книги из books_genre
test_get_book_genre_by_name: проверка на вывод жанра книги по ее имени
test_get_books_with_specific_genre_by_genre: проверка на вывод книг по жанру
test_get_books_with_specific_genre_by_wrong_genre: негативная проверка на вывод книг по жанру НЕ из genre
test_get_books_for_children: проверка на вывод детских книг
test_add_book_in_favorites_not_added_in_favorites_book: проверка на добавление книги в избранное
test_add_book_in_favorites_added_in_favorites_book: негативная проверка на повторное добавление книги в избранное
test_add_book_in_favorites_not_added_dict_book: негативная проверка на добавление книги НЕ из books_genre
test_delete_book_from_favorites: проверка на удаление книги из избранного
test_delete_book_from_favorites_deleted_book: негативная проверка на удаление из избранного книги НЕ добавленной в избранное
test_get_list_of_favorites_books: проверка на получение списка избранных книг