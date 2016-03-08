from enum import Enum

class ProcessStatus(Enum):
    UNEXECUTED  = 0
    RUNNING = 1
    FINISH  = 2
    ERROR   = 9