import abc


class Classifier(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def train(self, x, y): pass

    @abc.abstractmethod
    def predict(self, x): pass
