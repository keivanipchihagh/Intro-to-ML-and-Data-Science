# Linear Regression with a Real Dataset using Pandas (Google Developers - Crash Course)
%tensorflow_version 2.x
import tensorflow as tf, numpy as np, pandas as pd
from matplotlib import pyplot as plt

training_data = pd.read_csv("https://download.mlcc.google.com/mledu-datasets/california_housing_train.csv") # read the training data
training_data["median_house_value"] /= 1000.0 # scale (mandatory)

# function which creates a new model
def create_model(learning_rate):
  model = tf.keras.Sequential()
  model.add(tf.keras.layers.Dense(units = 1, input_shape = [1]))
  model.compile(loss = 'mean_squared_error', optimizer = tf.keras.optimizers.RMSprop(learning_rate), metrics = [tf.keras.metrics.RootMeanSquaredError()])

  return model

# function which trains the model and tweaks the weights and bias
def train_model(model, dataframe, feature, label, epochs, batch_size):
  history = model.fit(dataframe[feature], dataframe[label], epochs = epochs, batch_size = batch_size)

  # Gather the trained model's weight and bias
  trained_weight = model.get_weights()[0]
  trained_bias = model.get_weights()[1]

  return history, trained_weight, trained_bias

def predict_house_values(model, training_data, n, feature, label):

  batch = training_data[feature][10000:10000 + n]
  predicted_values = model.predict_on_batch(x = batch)

  print("feature   label          predicted")
  print("  value   value          value")
  print("          in thousand$   in thousand$")
  print("--------------------------------------")
  for i in range(n):
    print ("%5.0f %6.0f %15.0f" % (training_data[feature][i],
                                   training_data[label][i],
                                   predicted_values[i][0] ))  

def graph(df, history, trained_weight, trained_bias, feature, label):
  # loss
  plt.xlabel("Epoch")
  plt.ylabel("Root Mean Squared Error")
  plt.plot(pd.DataFrame(history.history)["root_mean_squared_error"], history.epoch, label = "Loss", c = "g")
  plt.legend()
  plt.show()

  random_examples = df.sample(n=200)
  plt.plot(random_examples[feature], random_examples[label], '.')

  plt.xlabel(feature)
  plt.ylabel(label)
  x0 = 0
  y0 = trained_bias
  x1 = 10000
  y1 = trained_bias + (trained_weight * x1)
  plt.plot([x0, x1], [y0, y1], c = 'r')
  plt.show()


learning_rate = 0.01
epochs = 30
batch_size = 24

feature = "total_rooms"  # the total number of rooms on a specific city block.
label="median_house_value" # the median value of a house on a specific city block.

model = create_model(learning_rate) # create the model
history, trained_weight, trained_bias = train_model(model, training_data, feature, label, epochs, batch_size) # train the model
graph(training_data, history, trained_weight, trained_bias, feature, label) # draw statistics

predict_house_values(model, training_data, 10, feature, label)
