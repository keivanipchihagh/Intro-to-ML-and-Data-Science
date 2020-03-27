# Simple supervised learning algorithm (Perceptron - CNN) to convert celsius to fahrenheit

import numpy, math, random

bias = random.random()
learningRate = 0.00001
weights = [random.random() for i in range(2)]

def Perceptron(inputs, target):

    # calculate the overall guess score
    output = (weights[0] * inputs)
    output += (bias * weights[1])

    # No-need for activation function here

    # Train the model like this
    error = target - output
    weights[0] += (error * learningRate * inputs)
    weights[1] += (error * learningRate * bias)

# Train perceptron for a lot of cycles (2.5M)
for i in range(2500000):
    Perceptron(0, 32)
    Perceptron(8, 46.4)
    Perceptron(15, 59)
    Perceptron(22, 71.6)

# 38 celsius equals to??
output = (weights[0] * 38)
output += (bias * weights[1])
print(output)
print(weights)
