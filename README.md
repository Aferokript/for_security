# Консоль безопасности банка

Код написан для сотрудников банка T-Bank. Вы не можете пользоваться им без доступа к БД, но можете использовать в учебных целях или для оценки его качества.

## Как установить?

Python3 уже должен быть установлен. Затем используйте pip (или pip3, если есть конфликт с Python2) для установки зависимостей:
1. pip install -r requirements.txt
2. pip install django=5.2
3. pip install psycopg2-binary

## Переменные окружения:

Чтобы подключиться к базе данных вам нужно заполнить значения переменных окружения:
1. DB_HOST=
2. DB_PORT=
3. DB_NAME=
4. DB_USER=
5. DB_PASSWORD=
6. SECRET_KEY=REPLACE_ME

## Пример запуска:
Количество активных пропусков: 89
Количество пропусков: 100

## Настройка Django

Пример конфигурации `settings.py`:

```python
import os
from dotenv import load_dotenv

load_dotenv()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': os.environ['DB_HOST'],
        'PORT': os.environ['DB_PORT'],
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = os.environ['SECRET_KEY']

TIME_ZONE = 'Europe/Moscow'
USE_TZ = True
```

## Цели проекта

Код написан в образовательных целях Для онлайн-курса для веб-разработчиков dvmn.org

