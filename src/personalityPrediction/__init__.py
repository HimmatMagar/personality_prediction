import os
import sys
import logging


log_dir = "logging"

log_path = os.path.join(log_dir, "running_log.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
      level = logging.INFO,
      format = '[%(asctime)s: %(levelname)s: %(module)s: %(message)s]',
      handlers = [
            logging.FileHandler(log_path),
            logging.StreamHandler(sys.stdout)
      ]
)

logging = logging.getLogger(__name__)