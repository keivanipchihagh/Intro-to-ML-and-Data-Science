# Imports
from tensorflow import keras
import pandas as pd
import numpy as np

# Load data
train_df = pd.read_csv('datasets/linear/data/train.csv')
test_df = pd.read_csv('datasets/linear/data/test.csv')

# Shuffle data
np.random.shuffle(train_df.values)

# Build the model
model = keras.Sequential([
    keras.layers.Dense(units = 4, input_shape = (2,), activation = 'relu'),
    keras.layers.Dense(units = 2, activation = 'sigmoid')
])

# Compile the model
model.compile(
    optimizer = 'adam',
    loss = keras.losses.SparseCategoricalCrossentropy(from_logits = True),
    metrics = ['accuracy']
)

# Convert train data into numpy format
train_x = np.column_stack((train_df['x'].values, train_df['y'].values))
train_y = train_df['color'].values

# Train the model
model.fit(train_x, train_y, batch_size = 4, epochs = 3)

# Convert test data into numpy format
test_x = np.column_stack((test_df['x'].values, test_df['y'].values))
test_y = test_df['color'].values

# Evaluate the model
model.evaluate(test_x, test_y)