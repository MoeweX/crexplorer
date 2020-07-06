# Container Resource Explorer

This repository contains the code for the python3-based container resource explorer container (CRExplorer).

Typical CRExplorer workflow:
- Start the container for use in console (`docker run --name crexplorer --env LOGFILE="/log.txt" --env PING="8.8.8.8" -it hasenburg/crexplorer`) or as webserver (`docker run --name crexplorer --env LOGFILE="/log.txt" --env PORT=3000 --env PING="8.8.8.8" -it -p 3000:3000 --restart on-failure hasenburg/crexplorer`)
- Apply resource manipulation instructions to container, e.g., with `docker update --memory 50mb --memory-swap 50mb crexplorer` or `docker update --cpus 2.0 crexplorer`
- Start resource exploration by entering the amount of to be allocated memory in console or sending a GET request to the server, e.g., http://localhost:3000/run?max_memory=30
- Study results that are printed to console or written to `LOGFILE` (retrieve with `docker cp crexplorer:/log.txt .`)

If you cloned the [GitHub Repository](https://github.com/MoeweX/crexplorer), you can use `make` to build and run the container.

## Get CRExplorer

```bash
# install sources
pip3 install -r requirements.txt
```

A pre-build container is available in the [Docker Hub](https://hub.docker.com/repository/docker/hasenburg/crexplorer).
