from abc import ABCMeta, abstractclassmethod

class IProcess:
    __metaclass__ = ABCMeta

    @abstractclassmethod
    def exec(self): pass

    @abstractclassmethod
    def is_finished(self): pass

    @abstractclassmethod
    def add_process(self, IProcess): pass