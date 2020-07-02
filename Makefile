FORCE: build

REPO=hasenburg

build:
	docker build . --no-cache -t $(REPO)/crexplorer:latest

push:
	docker push $(REPO)/crexplorer

run:
	docker rm crexplorer || true
	docker run --name crexplorer -it $(REPO)/crexplorer
