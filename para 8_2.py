import logging
logging.basicConfig(level=logging.DEBUG,
                    filename="para 8.2_logs.log",
                    filemode="w",
                    format="we have message:%(asctime)s:@:%(levelname)s - %(message)s")

try:
    print(10/0)
except Exception:
    logging.exception("Exception")

