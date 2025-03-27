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

    def setUp(self):
        """Создание экземпляра BooksCollector перед каждым тестом."""
        self.collector = BooksCollector()

    def test_add_new_book(self):
        """Тестирование добавления новой книги."""
        self.collector.add_new_book("Книга 1")
        self.assertIn("Книга 1", self.collector.books_genre)
        self.collector.add_new_book("Книга 1")  # Повторное добавление
        self.assertEqual(len(self.collector.books_genre), 1)  # Должно оставаться 1

        # Книга с длинным названием
        long_title = "К" * 41
        self.collector.add_new_book(long_title)
        self.assertEqual(len(self.collector.books_genre), 1)  # Все еще 1, так как длинное название

    def test_set_book_genre(self):
        """Тестирование установки жанра книги."""
        self.collector.add_new_book("Книга 1")
        self.collector.set_book_genre("Книга 1", "Фантастика")
        self.assertEqual(self.collector.get_book_genre("Книга 1"), "Фантастика")
        self.collector.set_book_genre("Книга 1", "Неизвестный жанр")  # Неверный жанр
        self.assertEqual(self.collector.get_book_genre("Книга 1"), "Фантастика")  # Жанр не должен измениться

    def test_get_book_genre(self):
        """Тестирование получения жанра книги."""
        self.collector.add_new_book("Книга 1")
        self.collector.set_book_genre("Книга 1", "Фантастика")
        self.assertEqual(self.collector.get_book_genre("Книга 1"), "Фантастика")
        self.assertIsNone(self.collector.get_book_genre("Неизвестная книга"))  # Книга не существует

    def test_get_books_with_specific_genre(self):
        """Тестирование получения списка книг с определённым жанром."""
        self.collector.add_new_book("Книга 1")
        self.collector.set_book_genre("Книга 1", "Фантастика")
        self.collector.add_new_book("Книга 2")
        self.collector.set_book_genre("Книга 2", "Фантастика")
        self.collector.add_new_book("Книга 3")
        self.collector.set_book_genre("Книга 3", "Ужасы")

        self.assertEqual(self.collector.get_books_with_specific_genre("Фантастика"), ["Книга 1", "Книга 2"])
        self.assertEqual(self.collector.get_books_with_specific_genre("Ужасы"), ["Книга 3"])
        self.assertEqual(self.collector.get_books_with_specific_genre("Неизвестный жанр"), [])  # Неправильный жанр

    def test_get_books_genre(self):
        """Тестирование получения текущего словаря books_genre."""
        self.collector.add_new_book("Книга 1")
        self.collector.set_book_genre("Книга 1", "Фантастика")
        self.collector.add_new_book("Книга 2")
        self.collector.set_book_genre("Книга 2", "Ужасы")

        expected_output = {
            "Книга 1": "Фантастика",
            "Книга 2": "Ужасы"
        }
        self.assertEqual(self.collector.get_books_genre(), expected_output)

    def test_get_books_for_children(self):
        """Тестирование получения книг, подходящих детям."""
        self.collector.add_new_book("Книга 1")
        self.collector.set_book_genre("Книга 1", "Фантастика")
        self.collector.add_new_book("Книга 2")
        self.collector.set_book_genre("Книга 2", "Ужасы")
        self.collector.add_new_book("Книга 3")
        self.collector.set_book_genre("Книга 3", "Детективы")
        self.collector.add_new_book("Книга 4")
        self.collector.set_book_genre("Книга 4", "Мультфильмы")

        self.assertEqual(self.collector.get_books_for_children(),
                         ["Книга 1", "Книга 4"])  # Только фэнтези и мультфильмы

    def test_add_book_in_favorites(self):
        """Тестирование добавления книги в избранное."""
        self.collector.add_new_book("Книга 1")
        self.collector.set_book_genre("Книга 1", "Фантастика")
        self.collector.add_book_in_favorites("Книга 1")
        self.assertIn("Книга 1", self.collector.favorites)
        self.collector.add_book_in_favorites("Книга 1")  # Повторное добавление
        self.assertEqual(len(self.collector.favorites), 1)  # Должно остаться 1

    def test_delete_book_from_favorites(self):
        """Тестирование удаления книги из избранного."""
        self.collector.add_new_book("Книга 1")
        self.collector.set_book_genre("Книга 1", "Фантастика")
        self.collector.add_book_in_favorites("Книга 1")
        self.collector.delete_book_from_favorites("Книга 1")
        self.assertNotIn("Книга 1", self.collector.favorites)

    def test_get_list_of_favorites_books(self):
        """Тестирование получения списка избранных книг."""
        self.collector.add_new_book("Книга 1")
        self.collector.set_book_genre("Книга 1", "Фантастика")
        self.collector.add_book_in_favorites("Книга 1")
        self.collector.add_new_book("Книга 2")
        self.collector.set_book_genre("Книга 2", "Комедии")
        self.collector.add_book_in_favorites("Книга 2")

        self.assertEqual(self.collector.get_list_of_favorites_books(), ["Книга 1", "Книга 2"])


if __name__ == '__main__':
    unittest.main()
