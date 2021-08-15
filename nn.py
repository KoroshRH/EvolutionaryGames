import numpy as np


class NeuralNetwork():

    def __init__(self, layer_sizes):
        wMatrice = []
        bVector = []
        for i in range(len(layer_sizes) - 1):
            wMatrice.append(np.random.randn(layer_sizes[i+1], layer_sizes[i]))
            bVector.append(np.zeros((layer_sizes[i+1], 1)))
        self.wMatrice = wMatrice
        self.bVector = bVector
        self.layer_sizes = layer_sizes

    def activation(self, x):
        return 1/(1 + np.exp(-1 * x))

    def forward(self, x):
        layers = [x]
        for k in range(len(self.layer_sizes) - 1):
            layers.append(self.activation((self.wMatrice[k] @ layers[k]) + self.bVector[k]))
        return layers[len(layers) - 1]
