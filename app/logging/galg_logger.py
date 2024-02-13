import logging
import os.path
import sys

from app.configuration import config
from app.logging.handler import ColorizedStreamHandler
from logging.handlers import RotatingFileHandler

DEFAULT_FMT = logging.Formatter(
    '%(asctime)s.%(msecs)03d [%(levelname)8s] %(message)s',
    datefmt='%Y-%m-%dT%H:%M:%S')


def init_logger():
    config_dir = config.get_log_directory()

    if not os.path.exists(config_dir):
        os.makedirs(config_dir)

    log_file_path = os.path.join(config_dir, "galg-vision.log")

    handler = RotatingFileHandler(log_file_path, maxBytes=1024 * 1024 * 20,
                                  backupCount=10, mode='a')

    handler.setFormatter(DEFAULT_FMT)

    logging.root.setLevel(logging.DEBUG)
    screen_handler = ColorizedStreamHandler(sys.stdout)
    screen_handler.setFormatter(DEFAULT_FMT)
    logger_i = logging.getLogger()
    logger_i.setLevel(logging.DEBUG)
    logger_i.addHandler(handler)
    logger_i.addHandler(screen_handler)

    logger = logging.getLogger()
    logger.info( f"Log  file path {log_file_path}." )
    with open("app/resources/banner.txt") as f:
        logger.info(f.read())

    return logger_i

