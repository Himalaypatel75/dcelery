# DjangoContainer

Django deployment with container
Do checkout other branches.

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
