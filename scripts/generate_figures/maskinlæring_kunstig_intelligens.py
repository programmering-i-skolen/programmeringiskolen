import matplotlib.pyplot as plt 
import matplotlib as mpl 
import numpy as np

from generate_figure_common import figure_begin, figure_end, figure_save



###
### Linear spread
###

def f(x):
    return 4*x + 3
N = 100
x = np.linspace(0, 1, N)
y = f(x) + np.random.uniform(-1,1, N)

figure_begin()
plt.plot(x, y, "o")
plt.xlabel("x")
plt.ylabel("y")
figure_end()
figure_save("data_ml_linear")

###
### ML linear
###
import tensorflow as tf
from tensorflow.keras import layers

model = tf.keras.Sequential()
model.add(layers.Dense(1, activation="linear", input_shape=(1,)))

def loss(y, y_pred):
    return tf.math.reduce_mean((y-y_pred)**2)

model.compile(optimizer=tf.keras.optimizers.Adam(0.1),
              loss=loss)
model.summary()

model.fit(x, y, epochs=20)

x_fit = np.linspace(0, 1, 100)
y_fit = model.predict(x_fit)
figure_begin()
plt.plot(x, y, "o", label="data")
plt.plot(x_fit, y_fit, label="prediction")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
figure_end()
figure_save("linear_ml")


###
### Mer avansert modell
###

figure_begin()
x = np.linspace(-4, 3, 200)
y = x**4 + x**3 - 12*x**2
plt.plot(x, y, "o", label="data")
plt.xlabel("x")
plt.ylabel("y")
figure_end()
figure_save("polynomial_random")

###
### Mer avansert modell 2 
###
model = tf.keras.Sequential()
model.add(layers.Dense(10, activation="sigmoid", input_shape=(1,)))
model.add(layers.Dense(1, activation="linear"))

def loss(y, y_pred):
    return tf.math.reduce_mean((y-y_pred)**2)

model.compile(optimizer=tf.keras.optimizers.Adam(0.1),
              loss=loss)
              
history = model.fit(x, y, epochs=150)
x_fit = np.linspace(-4, 3, 100)
y_fit = model.predict(x_fit)

figure_begin()
plt.plot(x, y, "o", label="data")
plt.plot(x_fit, y_fit, label="modell")
figure_end()
figure_save("ml_polynomial")

###
### Loss 
###


