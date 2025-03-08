# A Dockerfile is a script that defines how to build a Docker image.
# A Docker image is a lightweight, standalone, and executable package that contains everything needed to run an application, 
# including the code, runtime, libraries, environment variables, and configuration files.
# You can build the Docker image by running `docker build . -t {{ cookiecutter.project_slug }}` from the root of the repository.
# Then, run the image with e.g. `docker run -it {{ cookiecutter.project_slug }} bash`.

ARG BASE_CONTAINER="python:{{cookiecutter.python_version}}-slim-bookworm" 
FROM ${BASE_CONTAINER}

RUN apt-get update && apt-get install -y git wget

# Install uv binary
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV PACKAGE_NAME={{cookiecutter.project_slug}}
ENV PACKAGE_DIR=/${PACKAGE_NAME}
RUN mkdir ${PACKAGE_DIR}
WORKDIR ${PACKAGE_NAME}
COPY . ${PACKAGE_DIR}

# Default entrypoint
ENTRYPOINT ["uv", "run"]

# Default run command
CMD ["scripts/example.py"]