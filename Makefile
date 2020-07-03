FORCE: build

REPO=hasenburg

build:
	docker build . -t $(REPO)/crexplorer:latest

push:
	docker push $(REPO)/crexplorer

run:
	docker stop crexplorer || true
	docker rm crexplorer || true
	docker run --name crexplorer --env LOGFILE="/log.txt" $(REPO)/crexplorer

run-server:
	docker stop crexplorer || true
	docker rm crexplorer || true
	docker run --name crexplorer --env LOGFILE="/log.txt" --env PORT=3000 -p 3000:3000 --restart on-failure  $(REPO)/crexplorer

get-log:
	docker cp crexplorer:/log.txt .
