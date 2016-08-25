build-docker-dev:
	cp project/requirements/development.txt docker/dev/requirements.txt
	cp project/requirements/common.txt docker/dev/common.txt
	cd docker/dev/ && docker build -t "platzi/jsonfield-dev" .
	rm -rf docker/dev/requirements.txt
	rm -rf docker/dev/common.txt

start-dev:
	cd docker/dev/ && docker-compose up -d

stop-dev:
	cd docker/dev/ && docker-compose stop
