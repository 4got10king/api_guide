# task_manager

Паттерн UOW https://github1s.com/cosmicpython/code/tree/chapter_06_uow

## Задание:
Необходимо реализовать REST API приложения для справочника Организаций, Зданий, Деятельности.

## Установка
1) Клонируйте репозиторий:

`git clone git@github.com:4got10king/task_manager.git`

2) Настройте переменные окружения в файле .env по env.template:

3) Поднимите контейнеры

`docker-compose up`
Также запуск без контейнеров:

`cd backend`
`poetry install`
`poetry run alembic upgrade head`
`poetry run python run.py`

Приложение запустится на том порте и хосте, котороый вы указали в env.

## Технологии
Python 3.12+
FastAPI: для создания и управления API
SQLAlchemy + SQLite: для работы с базой данных
Pydantic: для валидации данных и схем
Docker: для контейнеризации приложения
AsyncIO: для асинхронной обработки запросов и наложения водяного знака
Текущие возможности
Регистрация нового участника с обработкой аватарки и наложением водяного знака.
Оценка другого участника с возможностью отслеживания взаимных симпатий и отправки уведомлений.
Список участников с возможностью фильтрации по параметрам, сортировки и поиска по расстоянию от заданных координат.
## Команды API


Преимущества
Асинхронная обработка: Использование асинхронных функций для повышения производительности и улучшения отклика API.

Дополнительные задачи
