# MUSE2 data analysis

> :warning: **Note that this repository is currently a work in progress.** :warning:

This repository contains Python scripts and Jupyter notebooks for analysing and
visualising [MUSE2] data files.

We recommend using [uv] for installing dependencies and managing your virtual
environment.

## Usage

To get started:

1. [Download and install uv] following the instructions for your OS.

1. Install the package and dependencies and set up the virtual environment:

    ```bash
    uv sync
    ```

1. Activate the virtual environment, or just preface your commands with `uv run` to use
the virtual environment (see [uv activate] for more info):

    ```bash
    source .venv/bin/activate
    <command>
    ```

    or

    ```bash
    uv run <command>
    ```

There are some example notebooks in the [`notebooks`] folder to get you started.

[MUSE2]: https://github.com/EnergySystemsModellingLab/MUSE2
[uv]: https://docs.astral.sh/uv
[Download and install uv]: https://docs.astral.sh/uv/getting-started/installation/
[uv activate]: https://docs.astral.sh/uv/pip/environments/
[`notebooks`] ./notebooks

## Copyright

Copyright © 2026 Imperial College London
