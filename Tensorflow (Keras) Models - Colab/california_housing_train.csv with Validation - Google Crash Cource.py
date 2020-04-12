# Optimzed Linear Regression using Validation (Google Developers - Crash Course)
%tensorflow_version 2.x
import numpy as np, tensorflow as tf, matplotlib.pyplot as plt, pandas as pd

# create model function
def create_model(learning_rate):
  model = tf.keras.Sequential() # create the network
  model.add(tf.keras.layers.Dense(units = 1, input_shape = [1]))  # add layers
  model.compile(loss = 'mean_squared_error', optimizer = tf.keras.optimizers.RMSprop(learning_rate), metrics = [tf.keras.metrics.RootMeanSquaredError()])  # compile the model
  return model

# train model function
def train_model(model, dataset, feature, label, epochs, batch_size, validation_split):
  history = model.fit(dataset[feature], dataset[label], epochs = epochs, batch_size = batch_size, validation_split = validation_split, verbose = False) # train the model

  return history

def graph(epochs, training_loss, validation_loss):
  plt.xlabel('Epoch')
  plt.ylabel('Root Mean Squared Error (RMSE)')
  plt.plot(epochs[0:], training_loss[0:], label = "Training Loss")
  plt.plot(epochs[0:], validation_loss[0:], label = "Validation Loss")
  plt.legend()
  plt.show()

learning_rate = 0.01
epochs = 50
batch_size = 12
validation_split = 0.1  # allocate some training data for validation

# load data set
train_df = pd.read_csv("https://download.mlcc.google.com/mledu-datasets/california_housing_train.csv")
test_df = pd.read_csv("https://download.mlcc.google.com/mledu-datasets/california_housing_test.csv")

# scale values
train_df["median_house_value"] /= 1000.0
test_df["median_house_value"] /= 1000.0

print(test_df)

feature = "median_income"
label = "median_house_value"

shuffled_train_df = train_df.reindex(np.random.permutation(train_df.index)) # shuffle before use, otherwise validation and traning dataframes wont match (see datafram for more info)

model = create_model(learning_rate) # create the model
history = train_model(model, shuffled_train_df, feature, label, epochs, batch_size, validation_split)  # train the model

graph(history.epoch, history.history['root_mean_squared_error'], history.history['val_root_mean_squared_error'])  # draw statistics