# Описание проекта:

Реализован REST API CRUD для основных моделей проекта, для аутентификации примненяются JWT-токены.
В проекте реализованы пермишены, фильтрации, сортировки и поиск по запросам клиентов,
реализована пагинация ответов от API, установлено ограничение количества запросов к API.

## Запуск проекта:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Ogyrecheg/api_yatube.git
```

```
cd api_yatube
```

Cоздать и активировать виртуальное окружение:

```
py -3.7 -m venv venv
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

**Технологии:**
- Python
- Django
- SQlite
- DRF
- GitHub
- Simple-JWT

### Автор проекта:
студент когорты №17 [Шевченко Александр](https://github.com/Ogyrecheg)
