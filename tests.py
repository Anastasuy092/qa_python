import pytest
from main import BooksCollector


@pytest.fixture
def collector():
    return BooksCollector()
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
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize(  # Параметризованный тест для добавления одинаковых книг
        "book, expected_length",
        [
            ('Оно', 1),
            ('1984', 1),
            ('Гарри Поттер', 1)
        ]
    )
    def test_add_new_book_duplicate(self, collector, book, expected_length):
        collector.add_new_book(book)
        collector.add_new_book(book)
        assert len(collector.get_books_genre()) == expected_length

    def test_book_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert collector.get_book_genre('Гарри Поттер') == 'Фантастика'

    def test_get_book_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')
        assert collector.get_book_genre('Гарри Поттер') == ''

    def test_get_book_with_specific_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Гарри Поттер']

    def test_get_books_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        expected_result = {'Гарри Поттер': 'Фантастика'}  # Ожидаемый словарь
        assert collector.get_books_genre() == expected_result

    def test_get_books_for_children(self):
        collector = BooksCollector()

        collector.add_new_book('Алиса в стране чудес')
        collector.set_book_genre('Алиса в стране чудес', 'Фантастика')
        assert 'Алиса в стране чудес' in collector.get_books_for_children()

    def test_add_book_in_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Сновидения Эхо')
        collector.add_book_in_favorites('Сновидения Эхо')
        assert 'Сновидения Эхо' in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Сновидения Эхо')
        collector.add_book_in_favorites('Сновидения Эхо')
        collector.delete_book_from_favorites('Сновидения Эхо')
        assert 'Сновидения Эхо' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()

        collector.add_new_book('Сновидения Эхо')
        collector.add_new_book('1984')
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Сновидения Эхо')
        collector.add_book_in_favorites('1984')
        collector.add_book_in_favorites('Гарри Поттер')
        assert collector.get_list_of_favorites_books() == ['Сновидения Эхо','1984','Гарри Поттер']

    @pytest.mark.parametrize(
        "book_title",
        [
            "",  # Пустое название
            "A" * 101  # Слишком длинное название (допустим, лимит 100 символов)
        ]
    )
    def test_add_new_book_invalid_title(self, book_title):
        collector = BooksCollector()  # Создаем новый экземпляр BooksCollector

        collector.add_new_book(book_title)
        assert book_title not in collector.get_books_genre()


