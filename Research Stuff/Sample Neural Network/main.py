from NN import NeuralNetwork
import numpy as np

if __name__ == "__main__":
    inputs = np.array((
        [3, 1.5],
        [2, 1],
        [4, 1.5],
        [3, 1],
        [3.5, 0.5]
    ), dtype=float)

    # for now, we just use the first row from the inputs
    # for testing purposes.

    nn = NeuralNetwork(np.size(inputs, 1), 3, 1)
    output = nn.feed_forward(inputs[0])

    print(output)
