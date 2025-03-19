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
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

import unittest

class TestBooksCollector(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.collector = BooksCollector()

    def test_add_new_book(self):
        collector = TestBooksCollector.collector
        collector.add_new_book("Book 1")
        assert "Book 1" in collector.books_genre
        assert collector.books_genre["Book 1"] == ""

    def test_add_book_with_long_name(self):
        collector = TestBooksCollector.collector
        long_book_name = "B" * 41
        previous_count = len(collector.books_genre)
        collector.add_new_book(long_book_name)
        assert len(collector.books_genre) == previous_count  # Книга не должна быть добавлена

    def test_add_duplicate_book(self):
        collector = TestBooksCollector.collector
        collector.add_new_book("Book 1")
        collector.add_new_book("Book 1")  # Повторное добавление
        assert len(collector.books_genre) == 1  # Книга должна остаться одна

    def test_set_book_genre(self):
        collector = TestBooksCollector.collector
        collector.add_new_book("Book 1")
        collector.set_book_genre("Book 1", "Фантастика")
        assert collector.get_book_genre("Book 1") == "Фантастика"

    def test_set_genre_for_non_existent_book(self):
        collector = TestBooksCollector.collector
        collector.set_book_genre("Book 2", "Фантастика")  # Книга не существует
        assert collector.get_book_genre("Book 2") is None

    def test_set_non_existing_genre(self):
        collector = TestBooksCollector.collector
        collector.add_new_book("Book 1")
        collector.set_book_genre("Book 1", "Неизвестный жанр")
        assert collector.get_book_genre("Book 1") == "Фантастика"  # Жанр не должен измениться

    def test_get_book_genre_existing_book(self):
        collector = TestBooksCollector.collector
        collector.set_book_genre("Book 1", "Фантастика")
        genre = collector.get_book_genre("Book 1")
        assert genre == "Фантастика"

    def test_get_book_genre_non_existing_book(self):
        collector = TestBooksCollector.collector
        genre = collector.get_book_genre("Non-existent Book")
        assert genre is None

    def test_get_book_genre_without_genre(self):
        collector = TestBooksCollector.collector
        collector.add_new_book("Book 3")
        genre = collector.get_book_genre("Book 3")
        assert genre == ""

    def test_get_books_genre_empty(self):
        empty_collector = BooksCollector()
        assert empty_collector.get_books_genre() == {}

    def test_get_books_genre_with_books(self):
        collector = TestBooksCollector.collector
        expected_genre_dict = {
            "Book 1": "Фантастика",
            "Book 2": "Ужасы",
            "Book 3": ""  # Книга без жанра
        }
        assert collector.get_books_genre() == expected_genre_dict

    def setUpClass(cls):
        cls.collector = BooksCollector()

    def test_get_book_genre_with_special_characters(self):
        """Тест на получение жанра книги с названием, содержащим специальные символы."""
        book_title = "Book @#!$%&*"
        self.collector.add_new_book(book_title)
        self.collector.set_book_genre(book_title, "Драма")
        genre = self.collector.get_book_genre(book_title)
        assert genre == "Драма"

    def test_get_book_genre_whitespace(self):
        """Тест на получение жанра книги с названием, состоящим только из пробелов."""
        book_title = "     "
        self.collector.add_new_book(book_title)
        self.collector.set_book_genre(book_title, "Комедия")
        genre = self.collector.get_book_genre(book_title)
        assert genre == "Комедия"

    def test_get_books_genre_with_varied_genres(self):
        """Тест на получение жанров для множества книг с различными жанрами."""
        self.collector.add_new_book("Book 1")
        self.collector.set_book_genre("Book 1", "Фантастика")
        self.collector.add_new_book("Book 2")
        self.collector.set_book_genre("Book 2", "Мелодрама")
        self.collector.add_new_book("Book 3")
        self.collector.set_book_genre("Book 3", "Приключения")

        expected_genres = {
            "Book 1": "Фантастика",
            "Book 2": "Мелодрама",
            "Book 3": "Приключения",
        }

        genres = self.collector.get_books_genre()
        assert genres == expected_genres

    def test_get_books_genre_no_genres_set(self):
        """Тест на получение жанров для книг, у которых не установлены жанры."""
        self.collector.add_new_book("Book 4")
        self.collector.add_new_book("Book 5")
        expected_genres = {
            "Book 4": "",
            "Book 5": "",
        }
        genres = self.collector.get_books_genre()
        assert genres == expected_genres

    def test_get_books_genre_with_mixed_entries(self):
        """Тест на получение жанров для книг с установленными и неустановленными жанрами."""
        self.collector.add_new_book("Book A")
        self.collector.set_book_genre("Book A", "Триллер")
        self.collector.add_new_book("Book B")  # Без жанра
        self.collector.add_new_book("Book C")
        self.collector.set_book_genre("Book C", "Научная фантастика")

        expected_genres = {
            "Book A": "Триллер",
            "Book B": "",
            "Book C": "Научная фантастика",
        }

        genres = self.collector.get_books_genre()
        assert genres == expected_genres

if __name__ == "__main__":
    unittest.main()
