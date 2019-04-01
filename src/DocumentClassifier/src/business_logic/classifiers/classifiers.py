from .classifier import Classifier
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier


class NeuralNetwork(Classifier):

    def __init__(self):
        self.__model = MLPClassifier(activation='relu', learning_rate="constant", learning_rate_init=0.001)

    def train(self, x, y):
        self.__model.fit(x, y)

    def predict(self, x):
        val = self.__model.predict_proba(x)

        return val


class KNearestNeighbour(Classifier):

    def __init__(self):
        self.__model = KNeighborsClassifier(n_neighbors=5)

    def train(self, x, y):
        self.__model.fit(x, y)

    def predict(self, x):
        val = self.__model.predict_proba(x)

        return val