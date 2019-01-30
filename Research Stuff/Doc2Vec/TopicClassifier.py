from sklearn.neural_network import MLPClassifier
import numpy as np


class TopicClassifier:
    """
    This class is used for the classification of documents to the topics.
    """

    def __init__(self):
        self.clf = MLPClassifier(activation='relu', learning_rate="constant", learning_rate_init=0.001)

    def train(self, x: np.array, y: np.array) -> None:
        """
        Train the neural network classifier
        :param x: input values
        :param y: predict labels
        """
        self.clf.fit(x, y)

    def predict(self, x: np.array) -> np.array:
        """
        Predict for given parameters
        :param x: A document vector
        :return: The topic predicted
        """
        val = self.clf.predict_proba(x)

        return val