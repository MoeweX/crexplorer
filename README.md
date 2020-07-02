# Container Resource Explorer

This repository contains the code for the python3-based container resource explorer container (CRExplorer).

Typical CRExplorer workflow:
- Start the container in interactive mode (`docker run -it hasenburg/crexplorer`)
- Apply resource manipulation instructions to container, e.g., with `docker update`
- Start resource exploration by entering the amount of to be allocated memory in interactive CRExplorer shell
- Study results that are printed to console
