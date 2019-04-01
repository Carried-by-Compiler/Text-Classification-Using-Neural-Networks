import abc


class Publisher(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def attach(self, observer): pass

    @abc.abstractmethod
    def notify_observers(self): pass


class Observer(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def update(self, args): pass
