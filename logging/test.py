import sys
import logging

fmt = "%(asctime)-15s %(levelname)s %(filename)s %(lineno)d %(process)d ##%(message)s"
logging.basicConfig(format=fmt, filename='logger.log', level=logging.DEBUG)

logging.debug('debug message')
logging.info('info message')
logging.warn('warn message')
logging.error('error message')
logging.critical('critical message')
