"""The main module for MUSE2 data analysis."""

from contextlib import suppress
from importlib.metadata import PackageNotFoundError, version

from .muse2 import find_muse2, run_muse2  # noqa: F401

with suppress(PackageNotFoundError):
    __version__ = version(__name__)
