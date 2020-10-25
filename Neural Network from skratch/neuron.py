import numpy as np

np.random.seed(0)

X = [[1, 2, 3, 2.5],
	 [2.0, 5.0, -1.0, 2.0],
	 [-1.5, 2.7, 3.3, -0.8]]

# Dense Layer 
class Layer_Dense:
	def __init__(self, n_inputs, n_nourons):
		self.weights = 0.1 * np.random.randn(n_inputs, n_nourons)
		self.biases = np.zeros((1, n_nourons))

	def forward(self, inputs):
		self.output = np.dot(inputs, self.weights) + self.biases

# Activation Function (ReLu)
class Activation_ReLu:
	def forward(self, inputs):
		self.output = np.maximum(0, inputs)


# Initialization
layer1 = Layer_Dense(2,5)
activation1 = Activation_ReLU()

layer1.forward(X)

activation1.forward(layer1.output)
print(activation1.output)