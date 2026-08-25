"""Tests for helpers.py."""

from pathlib import Path
from unittest.mock import Mock, patch

from muse2_data_analysis import helpers


@patch("muse2_data_analysis.helpers.run_muse2")
def test_get_example_output_dir_returns_existing_directory(
    run_muse2_mock: Mock, tmp_path: Path
) -> None:
    """Check that get_example_output_dir returns an existing output directory."""
    output_dir = tmp_path / "output"
    output_dir.mkdir()

    with patch.object(helpers, "_OUTPUT_DIR", output_dir):
        assert helpers.get_example_output_dir() == output_dir

    run_muse2_mock.assert_not_called()


@patch("muse2_data_analysis.helpers.run_muse2")
def test_get_example_output_dir_runs_example_when_missing(
    run_muse2_mock: Mock, tmp_path: Path
) -> None:
    """Check that get_example_output_dir runs the example when output is missing."""
    output_dir = tmp_path / "output"

    with patch.object(helpers, "_OUTPUT_DIR", output_dir):
        assert helpers.get_example_output_dir() == output_dir

    run_muse2_mock.assert_called_once_with(
        "example", "run", helpers.EXAMPLE_NAME, "--output-dir", str(output_dir)
    )
