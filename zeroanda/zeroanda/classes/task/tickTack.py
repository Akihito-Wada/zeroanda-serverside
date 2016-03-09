from datetime import datetime, timedelta

from zeroanda import utils

import math
import time

class TickTack:
    def __init__(self):pass

    def tickTack(self, task):
        if task == None:
            return

        while True:
            try:
                if task.hasProcess() == False:
                    break

                task.exec()

                # remain_time = self._targetdate.timestamp() - datetime.now().timestamp()
                # utils.info(remain_time)
                # if remain_time > self._scheduleModel.priority:
                # self.collect_prices2()
                # else:
                # i += 1

                nexttime = math.floor((datetime.now() + timedelta(seconds=1)).timestamp())
                duration = nexttime - datetime.now().timestamp()

                time.sleep(duration)
            except:
                print("exception.")
                break
        return