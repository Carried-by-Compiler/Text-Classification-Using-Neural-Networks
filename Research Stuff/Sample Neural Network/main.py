from neuralnet import NeuralNetwork
import numpy as np

if __name__ == "__main__":
    inputs = np.array([
        [2.3, 8.56],
        [3.43, 7.68],
        [1.32, 12.32],
        [2.34, 9.45],
        [1.87, 7.45],
        [3.76, 10.22],
        [1.65, 9.43],
        [2.87, 9.43],
        [3.0, 10.56],
        [7.68, 2.43],
        [6.45, 1.23],
        [9.56, 0.78],
        [5.34, 2.67],
        [8.21, 4.21],
        [7.54, 1.88],
        [6.77, 3.56],
        [9.0, 2.56],
        [8.0, 2.0],
        [2.31, 11.0],
        [7.0, 4.5]
    ], dtype=float)

    answers = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], dtype=float)

    nn = NeuralNetwork(2, 3, 1, 0.1)

    # training neural network
    for i in range(0, 100000):
        random_index = np.random.randint(0, np.size(answers))
        nn.train(inputs[random_index], answers[random_index])

    print("Training Complete\n")

    # Get insect dimension from end user
    input_width = float(input("Enter insect width:\t\t"))
    input_length = float(input("Enter insect length:\t"))

    # Get a trained guess
    output = nn.feed_forward([input_width, input_length])

    print("\nOUTPUT\n------")
    if output < 0.5:
        print("Ladybird")
    else:
        print("Stick Insect")