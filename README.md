# Проект «API для Yatube»

## Описание проекта.

Учебный проект для получения навыков, необходимых для создания REST API для Django-проекта.
API для социальной сети Yatube, в которой можно создавать посты, группы по интересам, а 
комментировать посты других пользователей а также подписываться на других пользователей.

## Установка:


Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/HusnutdinovRI/api_final_yatube.git
```

```
cd api_final_yatube
```

### *Установка на Windows:*

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/source/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

### *Установка на Mac OS и Linux:*

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
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



## Примеры:

### Получение публикаций

**Запрос**
```
GET /api/v1/posts/
```
**Ответ**
```
[
    {
        "id": 2,
        "author": "user1",
        "image": null,
        "text": "string",
        "pub_date": "2023-05-09T12:35:05.575663Z",
        "group": 1
    },
    {
        "id": 1,
        "author": "user1",
        "image": "http://127.0.0.1:8000/posts/temp.png",
        "text": "string",
        "pub_date": "2023-05-09T12:31:42.886919Z",
        "group": 1
    }
]
```
### Создание публикации

**Запрос**
```
POST /api/v1/posts/
```
```
{
    "text": "string",
    "image": "image": "data:image/png;base64,iVBORw...."
    "group": 1
}
```
**Ответ**
```
{
    "id": 1,
    "author": "user1",
    "image": "http://127.0.0.1:8000/posts/temp.png",
    "text": "string",
    "pub_date": "2023-05-09T12:31:42.886919Z",
    "group": 1
}
```
### Получение комментариев к записи

**Запрос**
```
GET /api/v1/posts/1/comments/
```
**Ответ**
```
[
    {
        "id": 2,
        "author": "user1",
        "post": 1,
        "text": "comment2",
        "created": "2023-05-09T12:37:53.835128Z"
    },
    {
        "id": 1,
        "author": "user1",
        "post": 1,
        "text": "comment",
        "created": "2023-05-09T12:36:56.122833Z"
    }
]
```
### Создание комментария к записи

**Запрос**
```
POST /api/v1/posts/1/comments/
```
**Ответ**
```
{
   "text": "comment"
}
```
```
{
    "id": 1,
    "author": "user1",
    "post": 1,
    "text": "comment",
    "created": "2023-05-09T12:36:56.122833Z"
}
```
### Получение списка сообществ

**Запрос**
```
GET /api/v1/groups/
```
**Ответ**
```
[
    {
        "id": 1,
        "title": "group_one",
        "slug": "one",
        "description": "Group_one"
    },
    {
        "id": 2,
        "title": "group_two",
        "slug": "group_two",
        "description": "group_two"
    }
]
```
### Подписка на автора

**Запрос**
```
POST /api/v1/follow/
```
```
{
    "following": "user2"
}
```
**Ответ**
```
{
    "user": "user1",
    "following": "user2"
}
```
### Посмотреть подписки пользователя

**Запрос**
```
GET /api/v1/follow/
```
**Ответ**
```
[
    {
        "user": "user1",
        "following": "user2"
    }
]
```


