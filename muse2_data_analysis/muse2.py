"""Tools for running the muse2 command-line program.

If the MUSE2_PATH environment variable is set, this will be used, otherwise muse2 will
be searched for on the PATH.
"""

import os
import shutil
import subprocess as sp
from pathlib import Path

_muse2_path: Path | None = None


def find_muse2() -> Path:
    """Get the path to muse2, if any.

    Raises an exception if muse2 is not found.
    """
    # Cache path
    global _muse2_path
    if _muse2_path:
        return _muse2_path

    path = os.getenv("MUSE2_PATH") or shutil.which("muse2")
    if not path:
        raise RuntimeError(
            "Could not find path to muse2. Either set the MUSE2_PATH environment "
            "variable or installing muse2 to your PATH (e.g. by running 'cargo "
            "install muse2')"
        )

    _muse2_path = Path(path)
    return _muse2_path


def run_muse2(*args: str) -> str:
    """Run muse2 with the specified arguments, returning combined stdout and stderr.

    Raises an exception if muse2 is not found.
    """
    muse2 = find_muse2()
    output = sp.run((muse2, *args), text=True, stdout=sp.PIPE, stderr=sp.STDOUT)
    if output.returncode != 0:
        raise RuntimeError(f"Error running muse2: {output.stdout}")

    return output.stdout
