import logging
logging.basicConfig(level=logging.DEBUG,
                    filename="para8.1_logs.log",
                    filemode="w",
                    format="we have message:%(asctime)s:@:(levelname)s - %(message)s")

logging.debug("debag")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")

logging.debug("debag2")
logging.info("info2")