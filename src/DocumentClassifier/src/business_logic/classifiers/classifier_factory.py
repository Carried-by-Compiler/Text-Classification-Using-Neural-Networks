from .classifiers import *


class ClassifierFactory:

    NEURAL_NET = "NEURAL_NETWORK"
    KNN = "KNN"

    @staticmethod
    def create_classifier(classifier_type):
        classifier = None

        if classifier_type == "NEURAL_NETWORK":
            classifier = NeuralNetwork()

        return classifier