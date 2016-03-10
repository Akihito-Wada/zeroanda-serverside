from abc import ABCMeta, abstractclassmethod
from multiprocessing import Process
import signal

from zeroanda.classes.task.interface.iprocess import IProcess
from zeroanda import utils

class AbstractProcess(IProcess):
    __metaclass__ = ABCMeta
    _task      = None

    def __init__(self, task):
        self._task = task
        self._create_job()

    @abstractclassmethod
    def _create_job(self): pass

    def exec(self):
        if self._is_condition() == False or self.is_running() or self.is_finished():
            return
        utils.info("self._jobs: " + str(len(self._jobs)))
        for job in self._jobs:
            # if job.is_alive() == True:
            #     break
            job.start()

        # [job.join() for job in self._jobs]

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
        return True
