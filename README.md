# Bronya

Bronya is a crawler for ecommerce data

*The project is a WIP, so expect major changes and additions.
Master branch is to be considered as always ready to use, with major changes/features introduced in feature branches.*

## Features

- Python 3.11+
- [Poetry](https://github.com/python-poetry/poetry) for dependency management
- SQLAlchemy ORM with alembic migrations
- RabbitMQ integrated via [pika](https://github.com/pika/pika/)
- configuration via ENV variables and/or `.env` file
- single file for each class
- Docker-ready (see [here](#docker))
- PM2-ready
- supports single-IP/rotating proxy config out of the box (see [here](#proxy-middleware))

## Installation

### Python Quickstart Guide
To create and run a new Scrapy project using this boilerplate, you need to:

1. Clone the repository.
2. `cp .env.example .env`
3. No docker:
   1. Have the following prerequisites: python 3.11+, poetry, mysqlclient libraries, etc
   2. `poetry install`
   3. `poetry shell`
   4. `scrapy`
4. Docker:
   1. Have the following prerequisites: docker, docker-compose
   2. `docker compose up -d database python`
   3. `docker compose exec python bash`
   4. `cd /var/app/python/src/`
   5. `poetry shell`
   6. `scrapy`