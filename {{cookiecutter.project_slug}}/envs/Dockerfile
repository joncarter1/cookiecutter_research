# A Dockerfile is a recipe for creating Docker images.
# A Docker image is a lightweight, stand-alone, executable package that includes everything needed to run a piece of software,
# including the code, a runtime, libraries, environment variables, and config files.

# You can build the Docker image by running `docker build . -t {{ cookiecutter.project_slug }}` from the root of the repository.
# Then, run the image with e.g. `docker run {{ cookiecutter.project_slug }} bash`.

# A base container provides the foundation for your image.
# We use the official Miniconda3 image as the base container.
# Default base: https://hub.docker.com/r/continuumio/miniconda3/tags
ARG BASE_CONTAINER="continuumio/miniconda3:24.3.0-0" 
FROM ${BASE_CONTAINER}

# Install application and testing requirements
ENV PACKAGE_NAME={{cookiecutter.project_slug}}
ENV PACKAGE_DIR=/${PACKAGE_NAME}
RUN mkdir ${PACKAGE_DIR}
COPY envs ${PACKAGE_DIR}/envs
WORKDIR ${PACKAGE_NAME}
RUN pip install -r envs/requirements_dev.txt && \
    pip cache purge

# .git needed to run pre-commit in the container.
COPY .pre-commit-config.yaml ${PACKAGE_DIR}
COPY .git ${PACKAGE_DIR}/.git/

# Install the Python package
COPY pyproject.toml ${PACKAGE_DIR}
COPY setup.cfg ${PACKAGE_DIR}
COPY MANIFEST.in ${PACKAGE_DIR}
COPY README.md ${PACKAGE_DIR}
COPY ${PACKAGE_NAME} ${PACKAGE_DIR}/${PACKAGE_NAME}/
COPY scripts ${PACKAGE_DIR}/scripts/
COPY tests ${PACKAGE_DIR}/tests/
RUN pip install -e .
