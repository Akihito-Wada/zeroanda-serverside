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
                if task.is_finished() == True:
                    break

                task.exec()

                nexttime = math.floor((datetime.now() + timedelta(seconds=1)).timestamp())
                duration = nexttime - datetime.now().timestamp()
                # utils.info(duration)
                time.sleep(duration)
            except Exception as e:
                utils.info(e)
                print("exception.")
                break
        return