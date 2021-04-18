# Imports
from tensorflow import keras
import pandas as pd
import numpy as np

# Load data
train_df = pd.read_csv('datasets/clusters_two_categories/data/train.csv')
test_df = pd.read_csv('datasets/clusters_two_categories/data/test.csv')

# Shuffle data
# np.random.shuffle(train_df.values)

# Encode data
one_hot_train_color = pd.get_dummies(train_df['color']).values
one_hot_train_marker = pd.get_dummies(train_df['marker']).values
train_labels = np.concatenate((one_hot_train_color, one_hot_train_marker), axis = 1)

one_hot_test_color = pd.get_dummies(test_df['color']).values
one_hot_test_marker = pd.get_dummies(test_df['marker']).values
test_labels = np.concatenate((one_hot_test_color, one_hot_test_marker), axis = 1)

# Build the model
model = keras.Sequential([
    keras.layers.Dense(units = 64, input_shape = (2,), activation = 'relu'),
    # keras.layers.Dropout(0.2),
    keras.layers.Dense(units = 64, activation = 'relu'),
    keras.layers.Dense(units = 9, activation = 'sigmoid')
])

# Compile the model
model.compile(
    optimizer = 'adam',
    loss = keras.losses.BinaryCrossentropy(from_logits = True),
    metrics = ['accuracy']
)

# Convert train data into numpy format
train_x = np.column_stack((train_df['x'].values, train_df['y'].values))


np.random.RandomState(seed = 42).shuffle(train_x)
np.random.RandomState(seed = 42).shuffle(train_labels)

# Train the model
model.fit(train_x, train_labels, batch_size = 4, epochs = 10)

# Convert test data into numpy format
test_x = np.column_stack((test_df['x'].values, test_df['y'].values))
test_y = test_df['color'].values

# Evaluate the model
model.evaluate(test_x, test_labels)

# Predict
prediction = model.predict(test_x)

print(np.round(prediction))