import logging


logging.basicConfig(level=logging.DEBUG, filename="logs.txt", filemode="w")
logging.info("This is start of application")
logging.warning("This is warning")
logging.error("This is error")
logging.critical("This is CRITICAL")