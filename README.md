
#  Django-Blog-Application

Here is a simple blog application created using Django and Django Rest Framework. It also possess CRUD (Create, Read, Update, Delete) functionalities.


## Setup Instructions

1. Clone this repository

2. Install dependencies:

```bash
  pip install -r requirements.txt
```

3. Run migrations:
```bash
  python manage.py makemigrations
  python manage.py migrate
```

4. Create a superuser:
```bash
  python manage.py createsuperuser
```

5. Run the Server:
```bash
  python manage.py runserver
```



## API Reference

1. POST API

#### List and Create

```http
  GET /api/posts/, POST /api/posts/
```

#### Retrieve, Update, Delete

```http
  GET /api/posts/<id>/, PUT /api/posts/<id>/, DELETE /api/posts/<id>/
```

#### Like the post

```http
  POST /api/posts/<id>/like/
```
2. Comment API

#### List & Create

```http
  GET /api/posts/<post_id>/comments/, POST /api/posts/<post_id>/comments/
```


