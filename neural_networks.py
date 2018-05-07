# coding: utf-8

import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


class NeuralNetwork(object):
    """ Create a neural network with three layers: input, hidden, output """
    def __init__(self, n_inputs, n_hidden, n_output, learning_rate=0.2):
        # start by randomly setting weights

        self.n_inputs = n_inputs
        self.n_hidden = n_hidden
        self.n_output = n_output

        self.w_hidden = np.random.uniform(size=(n_inputs, n_hidden))
        self.w_out = np.random.uniform(size=(n_hidden, n_output))

        self.learning_rate = learning_rate

    def predict(self, inputs):
        hidden = sigmoid(np.dot(inputs, self.w_hidden))
        output = sigmoid(np.dot(hidden, self.w_out))

        return output

    def train(self, X, Y):
        H = sigmoid(np.dot(X, self.w_hidden))
        Z = sigmoid(np.dot(H, self.w_out))

        E = Y - Z
        dZ = E * Z * (1 - Z)
        dH = dZ.dot(self.w_out.T) * H * (1 - H)

        self.w_hidden += self.learning_rate * np.dot(X.T, dH)
        self.w_out += self.learning_rate * np.dot(H.T, dZ)


if __name__ == "__main__":
    nn = NeuralNetwork(3, 3, 2)

    def dummy(a):
        b = [1, 0] if sum(a) > 1.5 else [0, 1]
        return np.array([b])

    for a in np.random.uniform(size=(100_000, 3)):
        nn.train(a.reshape(1, 3), dummy(a))

    for b in [0.1, 0.2, 0.3, 0.5, 0.9]:
        t = np.array([[b, b, b]])
        print(f"predict[{t}]: {nn.predict(t)}")
