#!/usr/bin/env python
import os
import subprocess

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

dotenv_example_contents = """\
# Values in this file can be loaded into the environment with ```from dotenv import load_dotenv(); load_dotenv()```
API_KEY=xxx
TEST_VAR=3
"""


def create_dotenv():
    """Create .env file for secrets."""
    dotenv_fp = os.path.join(PROJECT_DIRECTORY, ".env")
    with open(dotenv_fp, "w") as f:
        f.write(dotenv_example_contents)


def git_init():
    os.chdir(PROJECT_DIRECTORY)
    subprocess.call(["git", "init"])


def _remove(path):
    full_path = os.path.join(PROJECT_DIRECTORY, path)
    if os.path.isdir(full_path):
        os.rmdir(full_path)
    else:
        os.remove(os.path.join(PROJECT_DIRECTORY, path))


def remove_notebooks():
    _remove("notebooks/Demo.ipynb")
    _remove("notebooks")


if __name__ == "__main__":
    create_dotenv()
    if "Not open source" == "{{ cookiecutter.open_source_license }}":
        _remove("LICENSE")
    if "{{cookiecutter.full_name}}" == "Vitaly Kurin":
        remove_notebooks()
    git_init()
