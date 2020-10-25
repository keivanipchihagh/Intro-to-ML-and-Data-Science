import numpy as np
from matplotlib import pyplot as plt

np.random.seed(0)

X = [[1, 2, 3, 2.5],
		  [2.0, 5.0, -1.0, 2.0],
		  [-1.5, 2.7, 3.3, -0.8]]

class Layer_Dense:
	def __init__(self, n_inputs, n_nourons):
		self.weights = 0.1 * np.random.randn(n_inputs, n_nourons)
		self.biases = np.zeros((1, n_nourons))
	def forward(self, inputs):
		self.output = np.dot(inputs, self.weights) + self.biases

dense_layer_1 = Layer_Dense(4, 5)
dense_layer_2 = Layer_Dense(5, 2)

dense_layer_1.forward(X)
dense_layer_2.forward(dense_layer_1.output)

print(dense_layer_2.output)