import tensorflow as tf
from keras import Sequential
from keras.layers import Dense
from keras.optimizer_v1 import SGD
import numpy as np

mnist = tf.keras.datasets.mnist

(x_train, y_train),(x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

x_test = np.random.normal(x_test)

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dropout(0.7),
  tf.keras.layers.Dense(689, activation='sigmoid'),
  tf.keras.layers.Dropout(0.7),
  tf.keras.layers.Dense(10, activation='softmax'),
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=6, batch_size=100)  #0.0624

result1 = model.evaluate(x_train, y_train)
result = model.evaluate(x_test, y_test)

print('\nTrain Acc:', result1[1])
print('\nTest Acc:', result[1])

