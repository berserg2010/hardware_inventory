### Установка Docker

https://docs.docker.com/engine/install/

### Создание миграции, регистрация суперпользователя

    docker-compose run web python manage.py makemigrations
    docker-compose run web python manage.py migrate
>
    docker-compose run web python manage.py createsuperuser

Потребуется ввести `Username` и `Password`.


### Иницыализация данных приложений
    docker-compose run web python manage.py loaddata <app>/fixtures/init_<app>.json


### Запуск контейнеров

При первом запуске:

    docker-compose up --build

В дальнейшем:

    docker-compose up

### Запуск unit тестов
    docker-compose run web pytest


### Снятие копии с базы данных приложения
    docker-compose run web python manage.py dumpdata <app> --indent 2 --output dump_<app>.json
