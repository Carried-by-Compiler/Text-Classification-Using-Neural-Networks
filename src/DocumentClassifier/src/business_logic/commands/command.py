import abc


class Command(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def execute(self): pass
