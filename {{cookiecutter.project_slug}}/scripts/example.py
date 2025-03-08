"""Example script that uses Hydra for configuration.

https://hydra.cc/
"""
from dotenv import load_dotenv
import hydra
import os
import logging
from {{cookiecutter.project_slug}}.utils import func, func2


logger = logging.getLogger(__name__) # Hydra configures logging for us.

# Run python example.py --cfg job to print out the composed configuration
# rather than run the application.
@hydra.main(version_base=None, config_path='config', config_name='main')
def main(cfg) -> None:
    logger.info("Starting script....")
    test_var = os.environ.get("TEST_VAR") # This is set in the .env file
    logger.info(f"Value of TEST_VAR environment variable is {test_var}")
    logger.info(f"Value of input_val is {cfg.input_val}")
    logger.debug("This is a debug statement.")
    logger.info("This is a debug statement.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message")
    func(a=cfg.input_val)
    func2(a=cfg.input_val)
    logger.info("Completed.")

if __name__ == "__main__":
    load_dotenv() # Load secrets from .env file.
    main()