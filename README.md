# cookiecutter_research

A cookiecutter template for ML research in Python.

This template aims to combine Python software development best practices with useful research extensions.

## Template structure
This template generates a project with the following structure.
```bash
envs/ # Environment files e.g. pip, Conda and Docker.
notebooks/ # Sensible place for Jupyter notebooks.
scripts/ 
    example.py # An example script
    config/ # Folder to store Hydra configuration files.
src/ # Python package location for your project.
tests/ # Contains example tests using the Pytest framework.
.env # Used for storing env vars. Kept out of version control.
.editorconfig # Used to define code formatting conventions.
.pre-commit-config.yaml # Configures automatic checks that run before git commits
.gitignore # Identifies file patterns to exclude from git
pyproject.toml # Python configuration file
setup.cfg # Package installation configuration file.
```

## Usage
From inside the directory you wish to generate a repository (e.g. `cd $HOME/code`), run:
```bash
cookiecutter https://github.com/joncarter1/cookiecutter_research.git
```
This will generate a project folder, whose name will be set by the `{{ project_slug }}` variable set during generation.

You can then install a dedicated Conda environment, and the project package in editable mode, by running
```bash
conda env create --file envs/environment.yaml
conda activate {{ project_slug }} # Replace with name of generated environment
pip install -e .
pre-commit install
```
Installing your research code as a Python package means that you can import the code from anywhere, e.g. within the notebooks or scripts folder, without having to worry about relative import locations, or modifying the Python path.

The `-e` flag means that the imported package stays up-to-date with the local code within the `src` folder. See e.g. [here](https://stackoverflow.com/questions/35064426/when-would-the-e-editable-option-be-useful-with-pip-install) for more information about editable installs and [here](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/) for why a `src` layout is useful.

`pre-commit install` sets up a tool called `pre-commit`, which automatically runs a number of checks on code staged for commit whenever you run `git commit`. If these checks fail, the `git commit` is aborted.

Tests for the project can be run with `pytest`.

By default, the generated Python package contains a `utils.py` module. This contains a function that will fail the tests, and code issues that will be flagged by `ruff` e.g. hard-coded credentials. These are designed to provide simple, instructive examples of the utility of the tools included in the project such as `ruff` and `pytest`.

## Credits
This cookiecutter draws heavily on Audrey Feldroy's Python software package template:
https://github.com/audreyfeldroy/cookiecutter-pypackage