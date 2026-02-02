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
the virtual environment (see [uv docs] for more info).

    To activate on Linux/macOS:

    ```bash
    source .venv/bin/activate
    <command>
    ```

    To activate on Windows:

    ```powershell
    .venv\Scripts\activate
    ```

    Or run the command directly:

    ```bash
    uv run <command>
    ```

1. Make sure the Python code can find your MUSE2 installation. (If you have not yet
installed MUSE2, [follow the instructions here][install-muse2].)

    There are two ways you can do this:

    1. Make sure the `muse2` executable is on your [`PATH`]:

        - [Instructions for Windows][windows-path]
        - [Instructions for Linux][linux-path]
        - [Instructions for macOS][macos-path]

        (If you installed MUSE2 with `cargo`, it should already be on your `PATH`.)

    1. Set the `MUSE2_PATH` environment variable to the full path of the `muse2`
       executable file.

       You can either do this by [setting the environment variable from within
       Jupyter][jupyter-envvar] or from your shell before you launch Jupyter notebook.

There are some example notebooks in the [`notebooks`] folder to get you started. You can
view these with Jupyter notebook, like so:

```bash
uv run jupyter notebook
```

If you are using Visual Studio Code, you can also view them directly in your IDE with
[the Jupyter extension].

[MUSE2]: https://github.com/EnergySystemsModellingLab/MUSE2
[uv]: https://docs.astral.sh/uv
[Download and install uv]: https://docs.astral.sh/uv/getting-started/installation/
[uv docs]: https://docs.astral.sh/uv/pip/environments/#creating-a-virtual-environment
[install-muse2]: https://energysystemsmodellinglab.github.io/MUSE2/#getting-started
[`PATH`]: https://en.wikipedia.org/wiki/PATH_(variable)
[windows-path]: https://stackoverflow.com/a/41895179
[linux-path]: https://unix.stackexchange.com/questions/3809/how-can-i-make-a-program-executable-from-everywhere
[macos-path]: https://apple.stackexchange.com/a/41586
[jupyter-envvar]: https://stackoverflow.com/a/44251637
[`notebooks`]: ./notebooks
[the Jupyter extension]: https://code.visualstudio.com/docs/datascience/jupyter-notebooks

## Copyright

Copyright © 2026 Imperial College London
