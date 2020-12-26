import logging

# create and configure logger
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"  # log name, time, and message
logging.basicConfig(filename="./Lumberjack.log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='w')
# filemode='w': overwrite the log file

# basicConfig: default log level is WARNING = 30;
# logger set to be >= (set level), ex: debug: 10 and above
logger = logging.getLogger()

# Test messages
logger.debug("Debug message.")
logger.info("Info message.")
logger.warning("Warning message.")
logger.error("Error message.")
logger.critical("Critical message.")

# print(logger.level)
# Level      |  Numeric value
# NOTSET        0
# DEBUG         10
# INFO          20
# WARNING       30
# ERROR         40
# CRITICAL      50
