from django.shortcuts import render
from django.http    import HttpResponse

from datetime import datetime, timedelta

from zeroanda import utils

from multiprocessing import Process

import math
import time


def index(request):
    ticktack = TickTack()
    task = Task()
    ticktack.tickTack(task)
    return HttpResponse(200)


class TickTack:
    def __init__(self):pass

    def tickTack(self, task):
        # if task == None:
        #     return
        count = 0
        while True:
            try:
                if count > 3:
                    break

                task.exec()

                # nexttime = math.floor((datetime.now() + timedelta(seconds=1)).timestamp())
                # duration = nexttime - datetime.now().timestamp()
                # utils.info(duration)
                time.sleep(3)

                count += 1
            except Exception as e:
                utils.info(e)
                print("exception.")
                break
        return

class Task:
    def __init__(self):
        self._jobs = []
        process = Process(target=self.test)
        process2 = Process(target=self.test)
        self.add_process(process)
        self.add_process(process2)

    def test(self):
        utils.info('exec test')

    def add_process(self, process):
        self._jobs.append(process)

    def exec(self):
        for job in self._jobs:
            utils.info(job.is_alive())
            job.start()
            utils.info(job.is_alive())
