# Linear Regression using Feedforward Neural Nwetwork (Google Developers - Crash Course)
%tensorflow_version 2.x
import numpy as np, tensorflow as tf, matplotlib.pyplot as plt

# function which creates a new model
def create_model(learning_rate):
  model = tf.keras.Sequential()
  model.add(tf.keras.layers.Dense(units = 1, input_shape = [1]))
  model.compile(loss = 'mean_squared_error', optimizer = tf.keras.optimizers.RMSprop(learning_rate), metrics = tf.keras.metrics.RootMeanSquaredError())
  return model

# function which trains the model and tweaks the weights and bias
def train_model(model, feature, label, epochs, batch_size):
  history = model.fit(feature, label, epochs = epochs, batch_size = batch_size)

  # Gather the trained model's weight and bias.
  trained_weight = model.get_weights()[0]
  trained_bias = model.get_weights()[1]

  return history, trained_weight, trained_bias

# function which plots the training process
def graph(features, labels, history, trained_weight, trained_bias):
  # feature/label
  plt.xlabel("feature")
  plt.ylabel("label")
  x0 = 0
  y0 = trained_bias
  x1 = features[-1]
  y1 = trained_bias + (trained_weight * x1)
  plt.plot([x0, x1], [y0, y1], c='r') # regression line
  plt.plot(features, labels, ".") # features & labels
  plt.show()

  # loss
  plt.xlabel("Epoch")
  plt.ylabel("Root Mean Squared Error")
  plt.plot(history.history['root_mean_squared_error'], history.epoch, label = "MSE", c = "g")
  plt.legend()
  plt.show()

# training data
features = ([1.0, 2.0,  3.0,  4.0,  5.0,  6.0,  7.0,  8.0,  9.0, 10.0, 11.0, 12.0])
labels   = ([5.0, 8.8,  9.6, 14.2, 18.8, 19.5, 21.4, 26.8, 28.9, 32.0, 33.8, 38.2])

learning_rate = 0.1
epochs = 100
batch_size = 12

model = create_model(learning_rate)
history, trained_weight, trained_bias = train_model(model, features, labels, epochs, batch_size)

graph(features, labels, history, trained_weight, trained_bias)
