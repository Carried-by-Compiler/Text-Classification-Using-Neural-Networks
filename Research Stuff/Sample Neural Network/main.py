from neuralnet import NeuralNetwork
import numpy as np

if __name__ == "__main__":
    inputs = np.array([
        [3, 1.5],
        [2, 1],
        [4, 1.5],
        [3, 1],
        [3.5, 0.5],
        [2, 0.5],
        [5.5, 1],
        [1, 1]
    ], dtype=float)

    answers = np.array([1, 0, 1, 0, 1, 0, 1, 0], dtype=float)

    nn = NeuralNetwork(2, 3, 1, 0.1)
    chosen_index = 2
    for i in range(0, 50000):
        random_index = np.random.randint(0, np.size(answers))
        nn.train(inputs[random_index], answers[random_index])

    output = nn.feed_forward([10, 7])

    print("INPUTS\n------")
    print(str(inputs[chosen_index]) + "\n")
    if output < 0.5:
        box = "Blue"
    else:
        box = "Red"

    print("OUTPUT\n------\n" + str(box))

"""

    

    nn = NeuralNetwork(2, 3, 1, 0.1)

    for i in range(0, 10):
        random_index = np.random.randint(0, np.size(answers))
        nn.train(inputs[random_index], answers[random_index])

    # for now, we just use the first row from the inputs
    # for testing purposes.

    output = nn.feed_forward(np.array([1, 1], dtype=float))
    print(output)
"""