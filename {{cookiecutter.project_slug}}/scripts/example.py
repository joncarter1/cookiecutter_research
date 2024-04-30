"""Example script that uses Hydra for configuration."""
from dotenv import load_dotenv
import hydra
import logging
from omegaconf import DictConfig
import os
from {{cookiecutter.project_slug}}.utils import func, func2, load_dotenv as load_dotenv_insecure

logger = logging.getLogger(__name__) # Hydra configures logging for us.

load_dotenv_insecure() # This is insecure. Use `load_dotenv`+ `.env` file..

# Run python example.py --cfg job to print out the composed configuration
# rather than run the application.
@hydra.main(version_base=None, config_path='config', config_name='main')
def main(cfg: DictConfig) -> None:
    secret_key = os.environ['SECRET_KEY']
    # In practice, you definitely don't want to log this...
    logger.info(f'Starting script with {secret_key=}.')
    logger.info("Starting script.")
    logger.debug("This is a debug statement.")
    logger.error("This is an error message")
    func(a=cfg.input_val)
    func2(a=cfg.input_val)
    logger.info("Completed.")

if __name__ == "__main__":
    main()