## Библиотека

Консольное приложение-библиотека для добавления/просмотра/удаления книг.

## Руководство по эксплуатации

Заходим в файл ```main.py``` и запускаем его. Далее на выбор будут предложены 6 команд:
- Добавить книгу
- Удалить книгу
- Поиск книги
- Отобразить все книги
- Изменить статус книги
- Выйти

Вводим одну из них и довольствуемся результатом.

## Более подробная документация

Класс ```Book```:

Служит для инициализирования и парсинга данных в словарь, а затем для создания книги (объекта класса, который будет являться книгой) на основе этого словаря.

Класс ```Library```:

Служит для проведения опреаций с объектами-книгами.

_load_books:

Получение книг из json файла. Если он не найден, то возвращается пустой список.
Protected (_) для указания, что он не предназначен для использования напрямую в глобальном коде.

_save_books:

Сохранение изменений (добавление/удаление) в json файле (далее коммит). Protected по той же причине.

add_book:

Генерирует уникальное id для книги и добавляет саму книгу с полученными данными в файл и коммитит.

remove_book:

Удаление книги из json файла и коммитит изменения.

_get_book_by_id:

Получение книги из файла по id путем прохода по всем элементам и выборки нужного. Protected по той же причине.
Используется в методах удаления и изменения статуса.

search_books:

Поиск книги по введенным значениям. Если ничего не передать, то будут выведены все книги.

change_status:

Изменение статуса книги на противоположный и коммит. Если пользователь введет что-то, что не является допустимым статусом, то последний изменен не будет.

show_all_books:

Вывод всех книг путем выборки каждой через цикл.

Функция ```main```:

Создается объект класса Library и далее запускается бесконечный цикл.
Для пользователя выводится меню доступных команд:
- ```1``` Создание книги с введенными данными с помощью функции ```add_book```
- ```2``` Удаление книги, но если по введенному id книга не будет найдена, то удаления не произойдет
- ```3``` Поиск книг по введенным значениям. Для начала год парсится в целое число (если он был введен, т.к. он передается в качестве строки).
Далее идет проход по результатам и выбираются нужные книги
- ```4``` Вывод всех книг с помощью функции ```show_all_books```
- ```5``` Изменение статуса книги, полученной по введенному id. Если введенный статус окажется недопустимым, то изменение не произойдет
- ```6``` Завершение программы с обычным кодом выхода

Ну и в конце конструкция if __name__ == '__main__' для проверки запуска программы при нахождении в данном файле и для самого запуска. 
