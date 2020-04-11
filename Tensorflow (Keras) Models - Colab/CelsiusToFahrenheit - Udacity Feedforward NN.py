%tensorflow_version 2.x
from __future__ import absolute_import, division, print_function, unicode_literals
import numpy as np, matplotlib.pyplot as plt, tensorflow as tf  # imports

# training data
celsius = np.array([-40, -10,  0,  8, 15, 22,  38, 12, 16, -5, 213])
fahrenheit = np.array([-40,  14, 32, 46, 59, 72, 100, 53, 60, 23, 415])

model = tf.keras.Sequential([tf.keras.layers.Dense(units = 1, input_shape = [1])])  # create dense layers
model.compile(loss = 'mean_squared_error', optimizer = tf.keras.optimizers.Adam(0.1)) # compile the network
training_process = model.fit(celsius, fahrenheit, epochs = 300, verbose = False)  # train the NN

# plot the loss magnitude/epoch
plt.xlabel("Epoch Number")
plt.ylabel("Loss Magnitude")
plt.plot(training_process.history["loss"], label = 'Loss', c = 'r')
plt.legend()
plt.show()

print(model.predict([100])) # Predict
print(model.predict([47])) # Predict
print(model.predict([1235])) # Predict
print(model.predict([-81])) # Predict
