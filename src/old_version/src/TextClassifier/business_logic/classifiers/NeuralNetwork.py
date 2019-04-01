from sklearn.neural_network import MLPClassifier
from .IClassifier import IClassifier
import numpy as np


class NeuralNetwork(IClassifier):
    """
    This class is a classification model that makes use of sklearn's
    neural network model
    """
    def __init__(self):
        self.clf = MLPClassifier(activation='relu', learning_rate="constant", learning_rate_init=0.001)

    def train(self, x: np.array, y: np.array) -> None:
        self.clf.fit(x, y)

    def predict(self, x: np.array) -> np.array:
        val = self.clf.predict_proba(x)

        return val

