import logging
import os

from django.conf import settings

class Logger(object):
    logger = logging.getLogger('trade')

    @classmethod
    def setLogFileName(cls, targetname):
        file_log = logging.FileHandler(filename=os.path.join(settings.BASE_DIR, 'logs', 'trades', targetname + ".log"))
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        file_log.setFormatter(formatter)
        logging.getLogger().addHandler(file_log)

    @classmethod
    def info(cls, value):
        cls.logger.info(value)
