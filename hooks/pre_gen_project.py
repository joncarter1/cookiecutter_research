import re
import shutil
import sys


def check_executable_available(executable: str) -> bool:
    return shutil.which(executable) is not None


if not check_executable_available("uv"):
    print(
        "ERROR: uv is not available. Please install it before continuing. Instructions can be found at: https://docs.astral.sh/uv/getting-started/installation/)"
    )
    sys.exit(1)


MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"

module_name = "{{ cookiecutter.project_slug}}"

if not re.match(MODULE_REGEX, module_name):
    print(
        "ERROR: The project slug (%s) is not a valid Python module name. Please do not use a - and use _ instead"
        % module_name
    )

    # Exit to cancel project
    sys.exit(1)
