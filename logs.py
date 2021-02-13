import logging

# create and configure logger
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"  # log name, time, and message
logging.basicConfig(filename="logs.log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='w',
                    datefmt='%m/%d/%Y %H:%M:%S')
# filemode='w': overwrite the log file

# ---------------------------Alternative Logger config ----------------------- #
# Alternatively: set filename, level, format, and file handler individually; modular
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
#
# formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
#
# file_handler = logging.FileHandler('sample.log')
# file_handler.setLevel(logging.ERROR)
# file_handler.setFormatter(formatter)
#
# stream_handler = logging.StreamHandler()
# stream_handler.setFormatter(formatter)
#
# logger.addHandler(file_handler)
# logger.addHandler(stream_handler)
# ----------------------------------------------------------------------------- #


# Ex: logged message with traceback
def divide(x, y):
    """Divide Function"""
    try:
        result = x / y
    except ZeroDivisionError:
        logger.exception('Tried to divide by zero')  # log with traceback
    else:
        return result


# basicConfig: default log level is WARNING = 30;
# logger set to be >= (set level), ex: debug: 10 and above
logger = logging.getLogger(__name__)  # __name__ = '__main__'

# Log level and the messages
logger.debug("Debug message.")
logger.info("Info message.")
logger.warning("Warning message.")  # Default level
logger.error("Error message.")
logger.critical("Critical message.")

# DEBUG: Detailed information, typically of interest only when diagnosing problems.

# INFO: Confirmation that things are working as expected.

# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g.
# ‘disk space low’). The software is still working as expected.

# ERROR: Due to a more serious problem, the software has not been able to perform some function.

# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

# print(logger.level), default log level is WARNING = 30 (and everything >30)
# Level      |  Numeric value
# NOTSET        0
# DEBUG         10
# INFO          20
# WARNING       30
# ERROR         40
# CRITICAL      50
