import numpy as np


class NeuralNetwork:

    def __init__(self, i, hidden, output):
        self.input_nodes = i
        self.hidden_nodes = hidden
        self.output_nodes = output

        # randomize the weights
        # np.random.rand(<number-of-rows>, <number-of-columns>) -> returns a matrix of random value from 0 to 1
        self.weights_to_hidden = np.random.rand(self.hidden_nodes, self.input_nodes)
        self.weights_to_output = np.random.rand(self.output_nodes, self.hidden_nodes)

        self.bias_hidden = np.random.rand(self.hidden_nodes)
        self.bias_output = np.random.rand(self.output_nodes)

    def feed_forward(self, inputs):

        # Do matrix maths to calculate weighted sum of each hidden node
        values_hidden = np.dot(self.weights_to_hidden, inputs)
        values_hidden = np.add(values_hidden, self.bias_hidden)

        # Apply activation function to nodes in hidden layer
        for i in range(0, np.size(values_hidden)):
            values_hidden[i] = self.sigmoid(values_hidden[i])

        # Do matrix maths to calculate weighted sum of each output node
        values_output = np.dot(self.weights_to_output, values_hidden)
        values_output = np.add(values_output, self.bias_output)

        # Apply activation function to nodes in output layer
        for i in range(0, np.size(values_output)):
            values_output[i] = self.sigmoid(values_output[i])

        return values_output

    @staticmethod
    def sigmoid(x):
        return 1 / (1 + np.exp(-x))
