import signal
from abc import ABCMeta, abstractclassmethod

from zeroanda import utils
from zeroanda.classes.enums.process_status import ProcessStatus
from zeroanda.classes.task.interface.iprocess import IProcess


class AbstractProcess(IProcess):
    __metaclass__ = ABCMeta
    _task      = None

    def __init__(self, task):
        self._task = task
        self._create_job()
        self._set_status(ProcessStatus.waiting)

    @abstractclassmethod
    def _create_job(self): pass

    def exec(self):
        if self._is_condition() == False:
            return

        utils.info("self._jobs: " + str(len(self._jobs)))
        if 0 == len(self._jobs):
            # self._set_status(ProcessStatus.finish)
            return

        for job in self._jobs:
            job.start()

        self._set_status(ProcessStatus.running)

        # [job.join() for job in self._jobs]

    def is_runnable(self):
        result = self._get_status() == ProcessStatus.waiting and self.is_running() == False
        utils.info("self.status: " + self._get_status().name + ", self.is_running(): " + str(self.is_running()))
        utils.info('is_runnable: ' + str(result))
        return result

    def is_running(self):
        for job in self._jobs:
            if job.is_alive() == True:
               return True

        return False

    def is_finished(self):
        for job in self._jobs:
            utils.info(job.is_alive())
            utils.info(job.exitcode)
            utils.info(-signal.SIGTERM)
            if job.is_alive() == True or job.is_alive() == False and job.exitcode == None:
                return False

        self._set_status(ProcessStatus.finish)
        return True

    def _set_status(self, status):
        self.status = status

    def _get_status(self):
        return self.status
