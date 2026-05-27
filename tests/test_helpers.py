"""Tests for helpers.py."""

from pathlib import Path
from unittest.mock import Mock, patch

from muse2_data_analysis import helpers


@patch("muse2_data_analysis.helpers.run_muse2")
def test_get_example_input_dir_returns_existing_directory(
    run_muse2_mock: Mock, tmp_path: Path
) -> None:
    """Check that get_example_input_dir returns an existing input directory."""
    input_dir = tmp_path / "input"
    input_dir.mkdir()

    with patch.object(helpers, "_INPUT_DIR", input_dir):
        assert helpers.get_example_input_dir() == input_dir

    run_muse2_mock.assert_not_called()


@patch("muse2_data_analysis.helpers.run_muse2")
def test_get_example_input_dir_extracts_example_when_missing(
    run_muse2_mock: Mock, tmp_path: Path
) -> None:
    """Check that get_example_input_dir extracts the example when missing."""
    input_dir = tmp_path / "input"

    with patch.object(helpers, "_INPUT_DIR", input_dir):
        assert helpers.get_example_input_dir() == input_dir

    run_muse2_mock.assert_called_once_with(
        "example", "extract", helpers.EXAMPLE_NAME, str(input_dir)
    )


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
@patch("muse2_data_analysis.helpers.get_example_input_dir")
def test_get_example_output_dir_runs_example_when_missing(
    get_example_input_dir_mock: Mock, run_muse2_mock: Mock, tmp_path: Path
) -> None:
    """Check that get_example_output_dir ensures input exists and runs the model."""
    input_dir = tmp_path / "input"
    output_dir = tmp_path / "output"
    get_example_input_dir_mock.return_value = input_dir

    with patch.object(helpers, "_INPUT_DIR", input_dir):
        with patch.object(helpers, "_OUTPUT_DIR", output_dir):
            assert helpers.get_example_output_dir() == output_dir

    get_example_input_dir_mock.assert_called_once_with()
    run_muse2_mock.assert_called_once_with(
        "run", str(input_dir), "--output-dir", str(output_dir)
    )
