from enum import Enum

class ProcessStatus(Enum):
    waiting = 0
    running = 1
    finish  = 2