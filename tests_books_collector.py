import pytest
from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:
    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.books_genre) == 2

    @pytest.mark.parametrize('name, genre', [['Гордость и предубеждение и зомби', 'Комедии'],
                                             ['Что делать, если ваш кот хочет вас убить', 'Ужасы'],
                                             ['Крокодил Гена', 'Мультфильмы']])
    def test_set_book_genre_assign_genre_for_book(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.books_genre[name] == genre

    def test_get_book_genre_return_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Комедии')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Комедии'

    def test_get_books_with_specific_genre_return_genre_list_with_chosen_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Крокодил Гена')
        collector.set_book_genre('Крокодил Гена', 'Мультфильмы')
        collector.add_new_book('Мадагаскар')
        collector.set_book_genre('Мадагаскар', 'Мультфильмы')
        books_with_specific_genre = collector.get_books_with_specific_genre('Мультфильмы')
        assert 'Крокодил Гена' and 'Мадагаскар' in books_with_specific_genre

    def test_get_books_with_specific_genre_return_genre_list(self):
        collector = BooksCollector()
        collector.add_new_book('Аватар')
        collector.set_book_genre('Аватар', 'Приключения')
        assert collector.get_books_with_specific_genre('Приключения') == []

    def test_get_books_genre_return_books_genre(self):
        collector = BooksCollector()
        assert collector.get_books_genre() == collector.books_genre

    def test_get_books_for_children_add_books_to_books_for_children_list(self):
        collector = BooksCollector()
        collector.add_new_book('Крокодил Гена')
        collector.set_book_genre('Крокодил Гена', 'Мультфильмы')
        collector.add_new_book('Мадагаскар')
        collector.set_book_genre('Мадагаскар', 'Мультфильмы')
        books_for_children = collector.get_books_for_children()
        assert 'Крокодил Гена' and 'Мадагаскар' in books_for_children

    def test_get_books_for_children_return_empty_books_for_children_list(self):
        collector = BooksCollector()
        collector.add_new_book("Темная башня")
        collector.set_book_genre('Темная башня', 'Ужасы')
        collector.add_new_book('Аватар')
        collector.set_book_genre('Аватар', 'Приключения')
        assert collector.get_books_for_children() == []

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Темная башня")
        collector.set_book_genre('Темная башня', 'Ужасы')
        collector.add_book_in_favorites("Темная башня")
        assert "Темная башня" in collector.favorites

    def test_delete_book_from_favorites_remove_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Темная башня")
        collector.set_book_genre('Темная башня', 'Ужасы')
        collector.add_book_in_favorites("Темная башня")
        collector.delete_book_from_favorites("Темная башня")
        assert collector.favorites == []

    def test_get_list_of_favorites_books_return_list_of_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Темная башня")
        collector.set_book_genre('Темная башня', 'Ужасы')
        collector.add_book_in_favorites("Темная башня")
        collector.add_new_book('Крокодил Гена')
        collector.set_book_genre('Крокодил Гена', 'Мультфильмы')
        collector.add_book_in_favorites("Крокодил Гена")
        assert collector.favorites == collector.get_list_of_favorites_books()
