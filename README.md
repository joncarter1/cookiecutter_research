# cookiecutter_research

A cookiecutter template for ML research in Python.

This template aims to combine Python software development best practices with useful research extensions.

## Usage
From inside the directory you wish to generate a repository (e.g. `cd $HOME/code`), run:
```bash
cookiecutter https://github.com/joncarter1/cookiecutter_research.git
```

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

## Credits
This cookiecutter draws heavily on Audrey Feldroy's Python software package template:
https://github.com/audreyfeldroy/cookiecutter-pypackage