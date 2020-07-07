# Container Resource Explorer

This repository contains the code for the python3-based container resource explorer container (CRExplorer).

Typical CRExplorer workflow:
- Start the container for use in console (`docker run --name crexplorer --env PING="8.8.8.8" -it hasenburg/crexplorer`)
- Apply resource manipulation instructions to container, e.g., with `docker update --memory 50mb --memory-swap 50mb crexplorer` or `docker update --cpus 2.0 crexplorer`
- Start resource exploration by entering the amount of to be allocated memory in console
- Study results that are printed to console

If you cloned the [GitHub Repository](https://github.com/MoeweX/crexplorer), you can use `make` to build and run the container.
A pre-build container is available in the [Docker Hub](https://hub.docker.com/repository/docker/hasenburg/crexplorer).

## Environment variables

- `LOGFILE=<path to file>`: when set, all logs are not only printed to console but also written to this file
- `PORT`: when set, CRExplorer starts in server mode (see below)
- `PING`: when set, CRExplorer continuously pings the given address and logs results to console
- `EVENT_ENDPOINT`: WHEN SET, CRExplorer sends a GET request to this endpoint with query param `event_name=cpu` or `event_name=memory` when the CPU/memory benchmark has been completed

## Control via webserver

- Send request to `/run?max_memory=10` to start run, returns after run has completed
- Send request to `/prepare?max_memory=10` to prepare run execution
- Send request to `/state` to start run (in background) with prepared max_memory, returns immediatly
