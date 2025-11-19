build:
	docker-compose up --build

stop:
	docker-compose stop

up:
	docker-compose up

remove_all:
	docker-compose down --rmi all

logs:
	docker-compose logs

dev:
	docker-compose -f docker-compose.dev.yml up -d --build

shell:
	docker exec -it bronya-dev bash
