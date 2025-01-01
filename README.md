## Библиотека

Приложение, позволяющее читать и добавлять любые книги.

## Руководство по эксплуатации

- В корне проекта создаем файл .env
- В него добавляем переменные ```DB_USER```, ```DB_PASS``` и ```DB_NAME```
- Сохраняем и далее скачиваем все пакеты, которые перечислены в requirements.txt
- Переходим в каталог нашего проекта через терминал и вводим комманду
```python manage.py runserver```
- Довольствуемся результатом

## Документация

`config.py`

Подключение всех переменных окружения

(Далее следуют файлы из приложения books)

`auth.py`

Файл с классами аутентификации и авторизации по JWT токенам и сохранении их в куках

`decorators.py`

Файл с декоратором для авторизации по JWT (ибо в django из коробки нет авторизации по JWT)

`forms.py`

Всего одна форма для добавления и изменения книг на `addbooks.html` и `updatebooks.html`

`middleware.py`

Обновление access токена с помощью refresh токена

`models.py`

Всего три модели:
- Category с одним полем name, используется для категорий книг
- Book, основная модель для книги
- UserBooks, используется для коллекции книг определенного пользователя

`serializers.py`

Файл с сериалайзером для регистрации

`urls.py`

Подключение всех урлов для этого приложения, а зачем подключение их всех в основном `urls.py`

`views.py`

Файл с представлениями, в котором собраны:
- Добавление и удаление в коллекцию
- Регистрация
- Добавление книг
- Обновление книг
- Удаление книг
- Поиск
- Просмотр всех книг
- Просмотр книг в коллекции
- Подключение базовой страницы и страницы "О нас"

`templates/`

Файл со всеми html шаблонами.

`tests.py`

Файл с простыми API тестами.

## CI/CD

В пайплайне я добавил всего лишь две джобы: build и test.
Да, джобы по типу deploy нет, т.к у [render](https://render.com/) CI/CD уже настроено,
но на всякий случай закомментил джобу deploy.

## Примечание

Если у вас Хром, то фронт может отображаться некорректно.
Именно Хром, так как в других браузерах на хромиуме все отображается нормально.

Перед использованием не забудьте поставить в базе данных (Приложение заточено под PostgreSQL)
кодировку UTF-8, а также `LC_LOCATE` и `LC_CTYPE` на `ru_RU.UTF-8`
Просмотреть можно через sqlshell, используя команду \l

Можете делать с этим кодом что угодно, но если появятся вопросы, то вот почта:
```inksne@gmail.com```