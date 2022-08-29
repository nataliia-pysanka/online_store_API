cnf ?= .env
include $(cnf)
export $(shell sed 's/=.*//' $(cnf))

up:
	sudo docker-compose -f docker-compose.yml up --build

down:
	sudo docker-compose -f docker-compose.yml down

ps:
	sudo docker-compose ps -a

clear:
	sudo docker system prune -a

migrate:
	python3 manage.py migrate
seed:
	python3 manage.py seed