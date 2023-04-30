import logging

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)


class Logger:
    @staticmethod
    def log(message):
        logging.info(message)
