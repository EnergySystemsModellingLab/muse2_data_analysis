"""Tests for muse2.py."""

import subprocess as sp
from collections.abc import Generator
from pathlib import Path
from unittest.mock import Mock, patch

import pytest

from muse2_data_analysis import muse2


@pytest.fixture(autouse=True)
def reset_muse2_path() -> Generator[None]:
    """Reset the cached MUSE2 path before and after each test.

    Note this won't work if tests are run in parallel.
    """
    previous = muse2._muse2_path
    muse2._muse2_path = None
    yield
    muse2._muse2_path = previous


@patch("muse2_data_analysis.muse2.shutil.which")
@patch("muse2_data_analysis.muse2.os.getenv")
def test_find_muse2_uses_environment_variable(
    getenv_mock: Mock, which_mock: Mock
) -> None:
    """Check that find_muse2 prefers MUSE2_PATH over PATH lookup."""
    getenv_mock.return_value = "/tmp/muse2-from-env"

    assert muse2.find_muse2() == Path("/tmp/muse2-from-env")
    which_mock.assert_not_called()


@patch("muse2_data_analysis.muse2.shutil.which")
@patch("muse2_data_analysis.muse2.os.getenv")
def test_find_muse2_falls_back_to_path_lookup(
    getenv_mock: Mock, which_mock: Mock
) -> None:
    """Check that find_muse2 uses PATH lookup when no env var is set."""
    getenv_mock.return_value = None
    which_mock.return_value = "/tmp/muse2-from-path"

    assert muse2.find_muse2() == Path("/tmp/muse2-from-path")


@patch("muse2_data_analysis.muse2.shutil.which")
@patch("muse2_data_analysis.muse2.os.getenv")
def test_find_muse2_raises_when_binary_is_not_available(
    getenv_mock: Mock, which_mock: Mock
) -> None:
    """Check that find_muse2 raises if no muse2 binary can be found."""
    getenv_mock.return_value = None
    which_mock.return_value = None

    with pytest.raises(RuntimeError, match="Could not find path to muse2"):
        muse2.find_muse2()


@patch("muse2_data_analysis.muse2.sp.run")
@patch("muse2_data_analysis.muse2.find_muse2")
def test_run_muse2_returns_stdout(find_muse2_mock: Mock, run_mock: Mock) -> None:
    """Check that run_muse2 returns combined stdout/stderr output."""
    find_muse2_mock.return_value = Path("/tmp/muse2")
    run_mock.return_value = sp.CompletedProcess(
        args=(Path("/tmp/muse2"), "--version"),
        returncode=0,
        stdout="muse2 version output",
    )

    assert muse2.run_muse2("--version") == "muse2 version output"
    run_mock.assert_called_once_with(
        (Path("/tmp/muse2"), "--version"),
        text=True,
        stdout=sp.PIPE,
        stderr=sp.STDOUT,
        env={
            **muse2.os.environ,
            "MUSE2_USE_DEFAULT_SETTINGS": "1",
        },
        check=True,
    )


@patch("muse2_data_analysis.muse2.sp.run")
@patch("muse2_data_analysis.muse2.find_muse2")
def test_run_muse2_raises_runtime_error_on_subprocess_failure(
    find_muse2_mock: Mock, run_mock: Mock
) -> None:
    """Check that run_muse2 re-raises subprocess failures as RuntimeError."""
    find_muse2_mock.return_value = Path("/tmp/muse2")
    run_mock.side_effect = sp.CalledProcessError(
        1,
        (Path("/tmp/muse2"), "bad-arg"),
        output="combined output",
    )

    with pytest.raises(RuntimeError, match="Error running muse2: combined output"):
        muse2.run_muse2("bad-arg")
