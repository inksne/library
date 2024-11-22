import json

class Book:
    '''основной класс для книг (служит для добавления и получения книг)'''
    def __init__(self, title: str, author: str, year: int, status: str = 'в наличии'):
        '''инициализатор'''
        self.id = None
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_dict(self) -> dict:
        '''парсинг'''
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'status': self.status,
        }

    @staticmethod
    def from_dict(data: dict):
        '''создание объект класса по предоставленнм значениям'''
        book = Book(data['title'], data['author'], data['year'], data['status'])
        book.id = data['id']
        return book


class Library:
    '''проведение опреаций с книгами'''
    def __init__(self, data_file: str = 'data.json'):
        '''инициализатор'''
        self.data_file = data_file
        self.books = self._load_books()

    def _load_books(self):
        '''получение книг из json (если файл не найден, то возвращается пустой список)'''
        try:
            with open(self.data_file, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return [Book.from_dict(book) for book in data]
        except FileNotFoundError:
            return []

    def _save_books(self):
        '''сохранение изменений в json'''
        with open(self.data_file, 'w', encoding='utf-8') as file:
            json.dump([book.to_dict() for book in self.books], file, ensure_ascii=False, indent=4)

    def add_book(self, book: Book):
        '''добавление книг и генерация id'''
        book.id = len(self.books) + 1  
        self.books.append(book)
        self._save_books()

    def remove_book(self, book_id: int) -> bool:
        '''удаление книги из json'''
        book = self._get_book_by_id(book_id)
        if book:
            self.books.remove(book)
            self._save_books()
            return True
        return False

    def _get_book_by_id(self, book_id: int):
        '''получение книги по id'''
        for book in self.books:
            if book.id == book_id:
                return book
        return None

    def search_books(self, title = None, author = None, year = None):
        '''поиск книги по заголовку, автору и году'''
        result = self.books
        if title:
            result = [book for book in result if title.lower() in book.title.lower()]
        if author:
            result = [book for book in result if author.lower() in book.author.lower()]
        if year:
            result = [book for book in result if book.year == year]
        return result

    def change_status(self, book_id: int, new_status: str) -> bool:
        '''изменение статуса книги'''
        if new_status not in ['в наличии', 'выдана']:
            return False
        book = self._get_book_by_id(book_id)
        if book:
            book.status = new_status
            self._save_books()
            return True
        return False

    def show_all_books(self):
        '''вывод всех книг'''
        for book in self.books:
            print(f'id: {book.id},\n Заголовок: {book.title},\n Автор: {book.author},\n Год: {book.year},\n Статус: {book.status}\n')
            

def main():
    library = Library()

    while True:
        print('\nМеню:') # для отступа после вывода результата
        print('1. Добавить книгу')
        print('2. Удалить книгу')
        print('3. Поиск книги')
        print('4. Отобразить все книги')
        print('5. Изменить статус книги')
        print('6. Выйти')

        try:
            choice = input('Выберите операцию: ')

            if choice == '1':  # добавление книги с введенными значениями
                title = input('Введите название книги: ')
                author = input('Введите автора книги: ')
                year = int(input('Введите год издания: '))
                book = Book(title, author, year)
                library.add_book(book)
                print('Книга добавлена.')

            elif choice == '2':  # удаление книги по id
                book_id = int(input('Введите id книги для удаления: '))
                if library.remove_book(book_id):
                    print('Книга удалена.')
                else:
                    print('Книга не найдена.')

            elif choice == '3':  # поиск книги
                title = input('Введите название книги (или оставить пустым): ')
                author = input('Введите автора книги (или оставить пустым): ')
                year_input = input('Введите год издания (или оставить пустым): ')
                year = int(year_input) if year_input else None
                results = library.search_books(title, author, year)
                if results:
                    for book in results:
                        print(f'id: {book.id},\n Заголовок: {book.title},\n Автор: {book.author},\n Год: {book.year},\n Статус: {book.status}\n')
                else:
                    print('Книги не найдены.')

            elif choice == '4':  # отображение всех книг
                library.show_all_books()

            elif choice == '5':  # изменение статуса книги
                book_id = int(input('Введите id книги для изменения статуса: '))
                new_status = input('Введите новый статус (в наличии/выдана): ')
                if library.change_status(book_id, new_status):
                    print('Статус изменен.')
                else:
                    print('Ошибка изменения статуса.')

            elif choice == '6':  # выход
                print('Выход...')
                exit()

        except KeyboardInterrupt:
            print('Выход...')
            exit()

if __name__ == '__main__':
    main()