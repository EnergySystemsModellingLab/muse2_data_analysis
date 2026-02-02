"""Helper functions for notebooks."""

from pathlib import Path

from . import run_muse2

DATA_DIR = Path(__file__).parent.parent.absolute() / "data"
EXAMPLE_NAME = "muse1_default"
_INPUT_DIR = DATA_DIR / f"{EXAMPLE_NAME}_input"
_OUTPUT_DIR = DATA_DIR / f"{EXAMPLE_NAME}_output"


def get_example_input_dir() -> Path:
    """Get the directory for example input data.

    If the folder does not exist, we create it by extracting an example from muse2.
    """
    if _INPUT_DIR.exists():
        return _INPUT_DIR

    run_muse2("example", "extract", EXAMPLE_NAME, str(_INPUT_DIR))
    return _INPUT_DIR


def get_example_output_dir() -> Path:
    """Get the directory for example output data.

    If the folder does not exist, we create it by running an example model with muse2.
    """
    if _OUTPUT_DIR.exists():
        return _OUTPUT_DIR

    # Ensure INPUT_DIR exists
    get_example_input_dir()

    # Run the example model
    run_muse2("run", str(_INPUT_DIR), "--output-dir", str(_OUTPUT_DIR))
    return _OUTPUT_DIR
