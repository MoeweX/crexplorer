# Container Resource Explorer

This repository contains the code for the python3-based container resource explorer container (CRExplorer).

Typical CRExplorer workflow:
- Start the container in interactive mode (`docker run --name crexplorer -it hasenburg/crexplorer`)
- Apply resource manipulation instructions to container, e.g., with `docker update --memory 50mb --memory-swap 50mb crexplorer` or `docker update --cpus 2.0 crexplorer`
- Start resource exploration by entering the amount of to be allocated memory in interactive CRExplorer shell
- Study results that are printed to console

If you cloned the [GitHub Repository](https://github.com/MoeweX/crexplorer), you can use `make run` to start the container (takes care of old containers with the same name).
