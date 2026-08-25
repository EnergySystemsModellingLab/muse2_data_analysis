"""Helper functions for notebooks."""

from pathlib import Path

from . import run_muse2

DATA_DIR = Path(__file__).parent.parent.absolute() / "data"
EXAMPLE_NAME = "muse1_default"
_OUTPUT_DIR = DATA_DIR / f"{EXAMPLE_NAME}"


def get_example_output_dir() -> Path:
    """Get the directory for example output data.

    If the folder does not exist, we create it by running an example model with muse2.
    """
    if _OUTPUT_DIR.exists():
        return _OUTPUT_DIR

    # Run the example model
    run_muse2("example", "run", EXAMPLE_NAME, "--output-dir", str(_OUTPUT_DIR))
    return _OUTPUT_DIR
