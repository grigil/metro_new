## Порядок использования


Cначала собираем образы
```shell
docker-compose build
```
Поднимаем контейнеры
```shell
docker-compose up
```
Мигрируем нашу бд
```shell
docker-compose run --rm web alembic init migrations 
docker-compose run --rm web alembic revision --autogenerate -m "create inital tables"
docker-compose run --rm web alembic upgrade head
```
