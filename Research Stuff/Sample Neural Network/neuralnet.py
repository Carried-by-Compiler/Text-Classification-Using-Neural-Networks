import numpy as np
from scipy.special import expit as activation_function


class NeuralNetwork:

    def __init__(self, i, h, o, learning_rate):

        # set the number of nodes for each layer
        self.input_nodes = i
        self.hidden_nodes = h
        self.output_nodes = o

        # weights
        self.weights_to_hidden = np.random.rand(self.hidden_nodes, self.input_nodes)
        self.weights_to_output = np.random.rand(self.output_nodes, self.hidden_nodes)

        # biases
        self.biases_hidden = np.random.rand(self.hidden_nodes, 1)
        self.biases_output = np.random.rand(self.output_nodes, 1)

        # learning rate
        self.learning_rate = learning_rate

    def feed_forward(self, inputs):

        # Convert input to column vector
        inputs = np.array(inputs, ndmin=2).T

        # Compute hidden node activations
        hidden_values = np.dot(self.weights_to_hidden, inputs)
        hidden_values = np.add(hidden_values, self.biases_hidden)
        hidden_values = activation_function(hidden_values)

        #Computer output node activations
        output_values = np.dot(self.weights_to_output, hidden_values)
        output_values = np.add(output_values, self.biases_output)
        output_values = activation_function(output_values)

        return output_values

    def train(self, inputs, answers):

        # Convert parameters to column vectors
        inputs = np.array(inputs, ndmin=2).T
        answers = np.array(answers, ndmin=2).T

        # Get a vector of all the guesses the neural network makes
        hidden_values = np.dot(self.weights_to_hidden, inputs)
        hidden_values = np.add(hidden_values, self.biases_hidden)
        hidden_values = activation_function(hidden_values)

        output_values = np.dot(self.weights_to_output, hidden_values)
        output_values = np.add(output_values, self.biases_output)
        output_values = activation_function(output_values)

        # Adjust weights hidden -> output
        output_errors = np.subtract(answers, output_values)
        temp = output_errors * output_values * (1.0 - output_values)
        temp = self.learning_rate * temp

        delta_weights_ho = np.dot(temp, output_values.T)
        self.weights_to_output = np.add(self.weights_to_output, delta_weights_ho)
        self.biases_output = np.add(self.biases_output, temp)

        # Adjust weights input -> hidden
        hidden_errors = np.dot(self.weights_to_output.T, output_errors)
        temp = hidden_errors * hidden_values * (1.0 - hidden_values)
        temp = self.learning_rate * temp

        delta_weights_ih = np.dot(temp, inputs.T)
        self.weights_to_hidden = np.add(self.weights_to_hidden, delta_weights_ih)
        self.biases_hidden = np.add(self.biases_hidden, temp)
