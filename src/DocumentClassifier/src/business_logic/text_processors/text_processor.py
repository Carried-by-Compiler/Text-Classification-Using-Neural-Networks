import abc


class TextProcessor(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def process_text(self, text): pass