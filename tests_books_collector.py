import pytest
from main import BooksCollector

class TestBooksCollector:
    
    # Тесты для add_new_book 
    # Проверяем корректность добавления новых книг с разными названиями
    @pytest.mark.parametrize('name, expected', [
        ('Мастер и Маргарита', True),
        ('', False),
        ('X' * 41, False),
        ('X' * 40, True)
    ])
    def test_add_new_book(self, collector, name, expected):
        collector.add_new_book(name)
        assert (name in collector.get_books_genre()) == expected

    # # Тестирование метода set_book_genre() - валидные случаи
    def test_set_book_genre_valid(self, collector):
        collector.add_new_book('Преступление и наказание')
        collector.set_book_genre('Преступление и наказание', 'Детективы')
        assert collector.get_book_genre('Преступление и наказание') == 'Детективы'
    # Тестирование метода set_book_genre() - невалидные случаи
    def test_set_book_genre_invalid(self, collector):
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Несуществующий жанр')
        assert collector.get_book_genre('1984') == ''
    
    # Тест только для add_new_book
    def test_add_new_book(self, collector):
        collector.add_new_book('Мастер и Маргарита')
        assert 'Мастер и Маргарита' in collector.books_genre  # Прямой доступ к словарю
    # Тест только для get_book_genre
    def test_get_book_genre(self, collector):
        collector.books_genre = {'Убийство в Восточном экспрессе': 'Детективы'}
        assert collector.get_book_genre('Убийство в Восточном экспрессе') == 'Детективы'
    # Проверяем, что set_book_genre устанавливает жанр при использовании книги из books_genre и жанра из genre
    def test_set_book_genre_valid_genre_is_set(self, collector):
        collector.add_new_book('Десять негритят')
        collector.set_book_genre('Десять негритят', 'Детективы')
        assert collector.books_genre['Десять негритят'] == 'Детективы'
    # Проверяем что get_books_with_specific_genre возвращает книги определенного жанра
    # Запрашиваем книги определенного жанра ('Фантастика')
    def test_get_books_with_specific_genre(self, collector):
        collector.add_new_book('Гарри Поттер и философский камень')
        collector.add_new_book('Оно')
        collector.set_book_genre('Гарри Поттер и философский камень', 'Фантастика')
        collector.set_book_genre('Оно', 'Ужасы')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Гарри Поттер и философский камень']

    # Проверяем что метод get_books_for_children возвращает только детскую книгу
    def test_get_books_for_children(self, collector):
        collector.add_new_book('Винни-Пух')
        collector.add_new_book('Дракула')
        collector.set_book_genre('Винни-Пух', 'Мультфильмы')
        collector.set_book_genre('Дракула', 'Ужасы')
        assert collector.get_books_for_children() == ['Винни-Пух']

    # Проверяем, что add_book_in_favorites добавляет книгу в избранное
    def test_add_book_in_favorites(self, collector):
        collector.add_new_book('Три товарища')
        collector.add_book_in_favorites('Три товарища')
        assert 'Три товарища' in collector.get_list_of_favorites_books()
    # Проверяем, что add_book_in_favorites не добавляет повторно книгу в избранное
    def test_add_book_in_favorites_twice(self, collector):
        collector.add_new_book('Маленький принц')
        collector.add_book_in_favorites('Маленький принц')
        collector.add_book_in_favorites('Маленький принц')
        assert len(collector.get_list_of_favorites_books()) == 1

    # Проверяем метод delete_book_from_favorites для удаления из избранного
    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book('Анна Каренина')
        collector.add_book_in_favorites('Анна Каренина')
        collector.delete_book_from_favorites('Анна Каренина')
        assert 'Анна Каренина' not in collector.get_list_of_favorites_books()

    # Проверяем, что метод get_list_of_favorites_books возвращает обе книги
    # Проверяем корректность работы со списком избранного
    def test_get_list_of_favorites_books(self, collector):
        collector.add_new_book('Скотный двор')
        collector.add_new_book('Мы')
        collector.add_book_in_favorites('Скотный двор')
        collector.add_book_in_favorites('Мы')
        assert collector.get_list_of_favorites_books() == ['Скотный двор', 'Мы']

    # Проверяем что метод get_book_genre возвращает правильный жанр
    def test_get_book_genre(self, collector):
        collector.add_new_book('Убийство в Восточном экспрессе')
        collector.set_book_genre('Убийство в Восточном экспрессе', 'Детективы')
        assert collector.get_book_genre('Убийство в Восточном экспрессе') == 'Детективы'
    
    
        