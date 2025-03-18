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

    def setUp(self):
        self.collector = BooksCollector()

    def test_add_new_book(self):
        self.collector.add_new_book("Book 1")
        self.assertIn("Book 1", self.collector.books_genre)
        self.assertEqual(self.collector.books_genre["Book 1"], "")

        # Проверка, что нельзя добавить книгу с более чем 40 символами
        long_book_name = "B" * 41
        self.collector.add_new_book(long_book_name)
        self.assertNotIn(long_book_name, self.collector.books_genre)

        # Проверка, что одна и та же книга не может быть добавлена дважды
        self.collector.add_new_book("Book 1")
        self.assertEqual(len(self.collector.books_genre), 1)

    def test_set_book_genre(self):
        self.collector.add_new_book("Book 1")
        self.collector.set_book_genre("Book 1", "Фантастика")
        self.assertEqual(self.collector.get_book_genre("Book 1"), "Фантастика")

        # Проверка установки жанра несуществующей книги
        self.collector.set_book_genre("Book 2", "Фантастика")
        self.assertIsNone(self.collector.get_book_genre("Book 2"))

        # Проверка установки несуществующего жанра
        self.collector.set_book_genre("Book 1", "Неизвестный жанр")
        self.assertEqual(self.collector.get_book_genre("Book 1"), "Фантастика")

    def test_get_books_with_specific_genre(self):
        self.collector.add_new_book("Book 1")
        self.collector.set_book_genre("Book 1", "Фантастика")
        self.collector.add_new_book("Book 2")
        self.collector.set_book_genre("Book 2", "Фантастика")
        self.collector.add_new_book("Book 3")
        self.collector.set_book_genre("Book 3", "Ужасы")

        books = self.collector.get_books_with_specific_genre("Фантастика")
        self.assertEqual(books, ["Book 1", "Book 2"])

        books = self.collector.get_books_with_specific_genre("Ужасы")
        self.assertEqual(books, ["Book 3"])

    def test_get_books_for_children(self):
        self.collector.add_new_book("Book 1")
        self.collector.set_book_genre("Book 1", "Детективы")  # Жанр с возрастным рейтингом
        self.collector.add_new_book("Book 2")
        self.collector.set_book_genre("Book 2", "Комедии")  # Без возрастного рейтинга
        self.collector.add_new_book("Book 3")
        self.collector.set_book_genre("Book 3", "Мультфильмы")  # Без возрастного рейтинга
        self.collector.add_new_book("Book 4")
        self.collector.set_book_genre("Book 4", "Ужасы")  # Жанр с возрастным рейтингом

        books_for_children = self.collector.get_books_for_children()
        self.assertEqual(books_for_children, ["Book 2", "Book 3"])

    def test_add_and_delete_book_from_favorites(self):
        self.collector.add_new_book("Book 1")
        self.collector.add_book_in_favorites("Book 1")
        self.assertIn("Book 1", self.collector.favorites)

        # Проверка добавления в избранное книги, которая там уже есть
        self.collector.add_book_in_favorites("Book 1")
        self.assertEqual(len(self.collector.favorites), 1)

        self.collector.delete_book_from_favorites("Book 1")
        self.assertNotIn("Book 1", self.collector.favorites)

        # Проверка удаления книги, которой нет в избранном
        self.collector.delete_book_from_favorites("Book 1")
        self.assertEqual(len(self.collector.favorites), 0)

    def test_get_list_of_favorites_books(self):
        self.collector.add_new_book("Book 1")
        self.collector.add_book_in_favorites("Book 1")
        self.assertEqual(self.collector.get_list_of_favorites_books(), ["Book 1"])

        self.collector.add_new_book("Book 2")
        self.collector.add_book_in_favorites("Book 2")
        self.assertEqual(set(self.collector.get_list_of_favorites_books()), {"Book 1", "Book 2"})


if __name__ == "__main__":
    unittest.main()
