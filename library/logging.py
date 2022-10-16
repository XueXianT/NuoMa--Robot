import logging
import os
from library import utils, constants
from logging.handlers import RotatingFileHandler

PAGE = 4096

DEBUG = logging.DEBUG
INFO = logging.INFO
WARNING = logging.WARNING
ERROR = logging.ERROR


def getLogger(name):
    """
    作用同标准模块 logging.getLogger(name)
    :returns: logger
    """
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(filename)s - %(funcName)s - line %(lineno)s - %(levelname)s - %(message)s"
    )

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    LOG_PATH = os.path.join(constants.LOGS_PATH, utils.getTime() + ".log")

    if not (os.path.isfile(LOG_PATH)):


    # FileHandler
    file_handler = RotatingFileHandler(
        LOG_PATH,
        maxBytes=1024 * 1024,
        backupCount=5,
    )

    file_handler.setLevel(level=logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
