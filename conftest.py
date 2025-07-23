conftest.py
#Фикстура collector - создает новый экземпляр класса для каждого теста
    @pytest.fixture
    def collector(self):
        return BooksCollector()