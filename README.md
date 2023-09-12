# DjangoContainer

**this is containes two branch one with celery intigration with django itself and other is creating stand alone celery instance.**

Reference :- **https://www.udemy.com/course/django-celery-mastery/**

Django deployment with container

Steps :-

This project have docker image you can deploy on docker.
clone repo.
docker-compose up -d --build
docker exec -it django /bin/sh

<-- SOME INFORMATION -->

Work Flow :-
django(message provider) -> redis(message broker) -> celery(celery worker) -> db(result backend)

About redis :-
redis is in memory data structure store that can be use as database cash message broker. becouse of how it work compare to traditional db it is known for allowing quick read and write operations.

Topic :-

1. celery task grouping
2. Task chaining
3. django inbuilt worker
4. independent celery worker
5. task rate limits (prevent over whelming system for task restriction.)
6. prioritization based on rabbitMQ (pip install pika)
7. passing arguments and returning results from celery tasks
8. https://docs.celeryq.dev/en/stable/userguide/calling.html (async vs delay)
9. monitoring celery workers and tasks with **flower** (monitoring, management, visualization) - https://pypi.org/project/django-flower/, https://flower.readthedocs.io/en/latest/
10. exception in celery
11. 