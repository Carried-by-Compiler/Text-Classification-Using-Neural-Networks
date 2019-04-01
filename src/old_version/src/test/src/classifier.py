import numpy as np
from sklearn.neural_network import MLPClassifier


class NN:

    def __init__(self):
        self.__topics = list()
        self.clf = MLPClassifier(activation='relu', learning_rate="constant", learning_rate_init=0.001)

    def train(self, x: np.array, y: np.array) -> None:
        self.clf.fit(x, y)

    def predict(self, x: np.array) -> np.array:
        val = self.clf.predict_proba(x)

        return val

    def get_topics(self): return self.__topics

    def add_topic(self, t: str):
        if t not in self.__topics:
            self.__topics.append(t)

    def get_topic_vector(self, t: str):
        topic_vec = list()
        for topic in self.__topics:
            if t == topic:
                topic_vec.append(1)
            else:
                topic_vec.append(0)

        return topic_vec