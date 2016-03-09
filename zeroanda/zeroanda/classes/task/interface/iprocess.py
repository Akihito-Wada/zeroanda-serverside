from abc import ABCMeta, abstractclassmethod

class IProcess:
    __metaclass__ = ABCMeta

    @abstractclassmethod
    def exec(self): pass

    @abstractclassmethod
    def isFinished(self): pass

    @abstractclassmethod
    def addProcess(self, IProcess): pass