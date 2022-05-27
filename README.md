# Project Foodgram

[![CI/CD Foodgram](https://github.com/photometer/foodgram-project-react/workflows/CI%2FCD%20Foodgram/badge.svg)](https://github.com/photometer/foodgram-project-react/actions/workflows/foodgram_workflow.yml)

Available at http://foodgram.ga/

---

<details>
  <summary> Админка </summary>

```py
username: photometer
password: admin
```

</details>

## Technologies

- Python;
- Django-Rest-Framework;
- Gunicorn;
- Docker/Docker-compose;
- Nginx;
- Yandex.Cloud;
- Github Actions.

## Description

 Online service where users can:

- creare recipes;
- follow other users and view their recipes;
- like recipes and add them to list of favorite recipes;
- add recipes to shopping list and download it in txt-format.

<details>
    <summary><h2> Installation </h2></summary>

- Clone repository to the local computer:

```py
https://github.com/photometer/foodgram-project-react/
```

- Сollect containers from `infra`:

```py
docker-compose up -d
```

- In **backend** container:

```py
docker-compose exec backend python manage.py migrate
docker-compose exec backend python manage.py collectstatic
docker-compose exec backend python manage.py createsuperuser
docker-compose exec backend python manage.py load_ingredients
```

</details>

## Backend author

[Androsova Elizaveta](https://github.com/photometer)  
