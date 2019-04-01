import abc
import numpy as np


class IClassifier(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def train(self, x: np.array, y: np.array) -> None: pass

    @abc.abstractmethod
    def predict(self, x: np.array) -> np.array: pass
