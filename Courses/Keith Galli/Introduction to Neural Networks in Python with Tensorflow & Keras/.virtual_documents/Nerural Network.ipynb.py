from tensorflow import keras
import pandas as pd
import numpy as np


train_df = pd.read_csv('datasets/linear/data/train.csv')

np.random.shuffle(train_df.values)
train_df.head()


model = keras.Sequential([
    keras.layers.Dense(units = 4, input_shape = (2,), activation = 'relu'),
    keras.layers.Dense(units = 2, activation = 'sigmoid')
])

model.compile(
    optimizer = 'adam',
    loss = keras.losses.SparseCategoricalCrossentropy(from_logits = True),
    metrics = ['acuracy']
)

x = np.column_stack((train_df['x'].values, train_df['y'].values))

model.fil(x, train_df['color'].values, batch_size = 16)





















