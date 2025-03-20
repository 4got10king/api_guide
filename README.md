# task_manager

Паттерн UOW https://github1s.com/cosmicpython/code/tree/chapter_06_uow

## Задание:
Необходимо реализовать REST API приложения для справочника Организаций, Зданий, Деятельности.

## Установка
1) Клонируйте репозиторий:

`git clone https://github.com/4got10king/api_guide.git`

или

`git@github.com:4got10king/api_guide.git`

2) Настройте переменные окружения в файле .env по env.template, в той же директории, что и env.template:

```
BACKEND_SERVER__PORT=8080
BACKEND_SERVER__HOST=0.0.0.0
BACKEND_SERVER__WORKERS=5
BACKEND_SERVER__METHODS=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"]
BACKEND_SERVER__HEADERS=["*"]
```

3) Поднимите контейнеры

`docker-compose up`


Также запуск без контейнеров:

`cd backend` ->
`poetry install` ->
`poetry run alembic upgrade head` ->
`poetry run python run.py`

либо(если есть make)

`cd backend` ->
`poetry install` ->
`make migrate` ->
`make run-server`

Приложение запустится на том порте и хосте, котороый вы указали в .env

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

GET - /activities
GET - /activities/{id}
GET - /activities/{id}/organizations

GET - /buildings
GET - /buildings/radius?lat={}&lon={}&radius={}

GET - /organizations/{}
POST - /organizations
GET - /organizations/building/{}
POST - /organizations/search


### Преимущества
Асинхронная обработка: Использование асинхронных функций для повышения производительности и улучшения отклика API.

## Дополнительные задачи
Закончить с тестами =)

## Ссылки

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
