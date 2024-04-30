{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

{{ cookiecutter.project_short_description }}


Environment set-up
--------

```
conda env create --file envs/environment.yaml
pre-commit install
```