import os
import logging

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)
