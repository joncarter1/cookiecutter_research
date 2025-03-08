{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

{{ cookiecutter.project_short_description }}


Environment set-up
--------
The Python environment for this project is managed using **uv**. Commands can be run with e.g.
```bash
uv run scripts/example.py
```
This will dynamically install necessary dependencies into a local virtual environment (`.venv`) for the project and run the provided script using that environment. More information on **uv** can be found [here](https://docs.astral.sh/uv/).

Commands can also be run using Docker:
```bash
docker build . -t image
docker run image pytest
docker run scripts/example.py
```

## Development

### Automatic code checks

Before commiting changes to Git, run:
```bash
pre-commit install
```
to configure a range of checks (configured in `.pre-commit-config.yaml`) that will run automatically whenever you run `git commit`!

Linting and formatting in this repository are handled by **ruff**. If you find the default linting and formatting rules of **ruff** too strict, it is simple to disable specific rules. See the `[tool.ruff.lint]` section of the `pyproject.toml` configuration file for an example of how to do this.

### Testing
Tests for this project should be stored under the `tests` folder and can be run with `uv run pytest`.
