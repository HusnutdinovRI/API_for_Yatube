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
## Примеры:

### Получение публикаций

```
GET /api/v1/posts/
```

### Создание публикации

```
POST /api/v1/posts/
```
```
{
    "text": "string",
    "image": "string",
    "group": 0
}
```

### Получение комментариев к записи

```
GET /api/v1/posts/{post_id}/comments/
```

### Создание комментария к записи

```
POST /api/v1/posts/{post_id}/comments/
```
```
{
    "text": "string"
}
```
### Получение списка сообществ

```
GET /api/v1/groups/
```

### Подписка на автора

```
POST /api/v1/follow/
```
```
{
    "following": "user1"
}
```




