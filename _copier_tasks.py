#!/usr/bin/env python
import os
import subprocess
import sys
import re
import shutil

# Get the destination directory - this is where the generated project will be
PROJECT_DIRECTORY = os.getcwd()


def check_executable_available(executable: str) -> bool:
    return shutil.which(executable) is not None


def validate_project_slug(project_slug):
    """Validate the project slug as a Python module name."""
    MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"

    if not re.match(MODULE_REGEX, project_slug):
        print(
            f"ERROR: The project slug ({project_slug}) is not a valid Python module name. Please do not use a - and use _ instead"
        )
        sys.exit(1)


def check_uv_available():
    """Check if uv is available."""
    if not check_executable_available("uv"):
        print(
            "ERROR: uv is not available. Please install it before continuing. Instructions can be found at: https://docs.astral.sh/uv/getting-started/installation/"
        )
        sys.exit(1)


def create_dotenv():
    """Create .env file for secrets."""
    dotenv_example_contents = """\
# Values in this file can be loaded into the environment with ```uv run --env-file .env script.py```
API_KEY=xxx
TEST_VAR=3
"""
    dotenv_fp = os.path.join(PROJECT_DIRECTORY, ".env")
    with open(dotenv_fp, "w") as f:
        f.write(dotenv_example_contents)


def git_init():
    """Initialize git repository."""
    os.chdir(PROJECT_DIRECTORY)
    subprocess.call(["git", "init"])


def remove(path):
    """Remove file or directory."""
    full_path = os.path.join(PROJECT_DIRECTORY, path)
    if os.path.isdir(full_path):
        os.rmdir(full_path)
    else:
        os.remove(full_path)


def remove_notebooks():
    """Remove notebooks for specific user."""
    remove("notebooks/Demo.ipynb")
    remove("notebooks")


if __name__ == "__main__":
    # Run pre-generation checks
    check_uv_available()

    # Get values from command line arguments
    project_slug = sys.argv[1] if len(sys.argv) > 1 else ""
    full_name = sys.argv[3] if len(sys.argv) > 3 else ""

    validate_project_slug(project_slug)

    create_dotenv()

    if full_name == "Vitaly Kurin":
        remove_notebooks()
