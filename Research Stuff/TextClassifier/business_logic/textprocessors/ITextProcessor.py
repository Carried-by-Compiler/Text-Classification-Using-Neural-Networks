import abc
import numpy


class ITextProcessor(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def process_text(self, text: str) -> numpy.array: pass
