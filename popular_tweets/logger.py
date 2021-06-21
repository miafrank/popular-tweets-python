import logging


class Logger:
    def __init__(self, clazz):
        logging.basicConfig(filename='example.log', format='%(asctime)s %(message)s',
                            datefmt='%Y-%m-%d %I:%M:%S %p', level=logging.DEBUG)
        self.logger = logging.getLogger(clazz)

    def info(self, msg):
        self.logger.info(msg)

    def warn(self, msg):
        self.logger.warning(msg)

    def debug(self, msg):
        self.logger.debug(msg)
        
    def error(self, msg):
        self.logger.error(msg)
