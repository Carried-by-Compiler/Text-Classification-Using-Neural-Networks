import abc


class GUI(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_unseen_text(self): pass

    @abc.abstractmethod
    def get_word(self): pass

    @abc.abstractmethod
    def display(self): pass
