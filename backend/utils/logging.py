import logging
import sys


def GetLogger(__name__):
    """ Returns a logger that streams into the console """
    logger = logging.getLogger(__name__)
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)
        consoleHandler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            f"%(asctime)s - %(levelname)s - %(name)s - %(funcName)s: %(lineno)d - %(message)s")
        consoleHandler.setFormatter(formatter)
        logger.addHandler(consoleHandler)
    return logger