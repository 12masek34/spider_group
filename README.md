## Deployment.

```
git clone git@github.com:12masek34/spider_group.git

cd spider_group/

docker-compose up --build

```

## Create superuser

```
docker exec -it web python manage.py createsuperuser

```

## Create token

```
docker exec -it web python manage.py drf_create_token <login_superuser>

```

## Run test

```
docker exec -it web pytest

```

### Реальзация ТЗ (см. task.txt)

Примеры использования api описаны в докстрингах app/view.py
