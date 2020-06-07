### Установка Docker

https://docs.docker.com/engine/install/

### Создание миграции, регистрация суперпользователя

    docker-compose run web python manage.py makemigrations
    docker-compose run web python manage.py migrate
>
    docker-compose run web python manage.py createsuperuser

Потребуется ввести `Username` и `Password`.


### Запуск контейнеров

При первом запуске:

    docker-compose up --build

В дальнейшем:

    docker-compose up

### Запуск unit тестов
    docker-compose run web pytest
