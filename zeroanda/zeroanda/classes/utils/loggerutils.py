from datetime import datetime
import logging
import os

from django.conf import settings

class Logger(object):
    logger = logging.getLogger('trade')

    @classmethod
    def setLogFileName(cls, targetname):
        file_log = logging.FileHandler(filename=os.path.join(settings.BASE_DIR, 'logs', 'trades', targetname + ".log"))
        formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
        file_log.setFormatter(formatter)
        # logging.getLogger().addHandler(file_log)
        logging.getLogger('trade').addHandler(file_log)

    @classmethod
    def setLogFileNameBySchedule(cls, scheduleModel):
        # filename = "trade_" + str(scheduleModel.id) + "_" + scheduleModel.presentation_time.strftime("%Y%m%d_%H%M%S") + "_" + datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = "trade_" + str(scheduleModel.id) + "_" + datetime.now().strftime("%Y%m%d_%H%M%S")
        cls.setLogFileName(filename)

    @classmethod
    def debug(cls, value):
        cls.logger.debug(value)

    @classmethod
    def warn(cls, value):
        cls.logger.warn(value)

    @classmethod
    def info(cls, value):
        cls.logger.info(value)

    @classmethod
    def error(cls, value):
        cls.logger.error(value)

    @classmethod
    def fatal(cls, value):
        cls.logger.fatal(value)

