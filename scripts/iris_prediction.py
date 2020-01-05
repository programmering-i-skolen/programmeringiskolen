import numpy as np 
import matplotlib.pyplot as plt

inputs = np.loadtxt("datasett/iris.csv", delimiter=",", usecols=(0,1,2,3), skiprows=1)
species = np.loadtxt("datasett/iris.csv", delimiter=",", usecols=(4), skiprows=1, dtype=str)

# Shuffle data 
indices = list(range(len(inputs)))
from random import shuffle
shuffle(indices)
inputs = inputs[indices]
species = species[indices]


categories = np.zeros(len(species), dtype="uint8")
categories[species == "setosa"] = 0
categories[species == "versicolor"] = 1
categories[species == "virginica"] = 2

category_matrix = np.zeros((len(species),3))
category_matrix[species=="setosa",0] = 1 
category_matrix[species=="versicolor", 1] = 1 
category_matrix[species=="virginica", 2] = 1 

import tensorflow as tf
from tensorflow.keras import layers 

model = tf.keras.Sequential()
model.add(layers.Dense(3, input_shape=(4,), activation="sigmoid"))
model.add(layers.Dense(3, activation="sigmoid"))

model.compile(optimizer=tf.keras.optimizers.Adam(0.01),
              loss="mse",
              metrics=["accuracy"])

model.summary() 

validation_split = 0.33
history = model.fit(inputs, category_matrix, epochs=4000, validation_split=validation_split, batch_size=200)

validation_index = int((1-validation_split)*len(inputs))
predictions = model.predict(inputs)

category_predictions = np.argmax(predictions, axis=1)

prediction_success = np.equal(category_predictions, categories)
print("validerings-suksessraten var", np.mean(prediction_success[validation_index:]))
print("trenings-suksessraten var", np.mean(prediction_success))


plt.figure(figsize=(3,3))
plt.semilogy(range(len(history.history["loss"])), history.history["loss"], label="$\mathrm{loss}_\mathrm{trening}$")
plt.semilogy(range(len(history.history["val_loss"])), history.history["val_loss"], label="$\mathrm{loss}_\mathrm{validering}$")
plt.show()

"""
names = ["Lengde begerblad", "Bredde begerblad", "Lengde Kronblad", "Bredde Kronblad"]

plt.figure(figsize=(4,4))
for i in range(3):
    for j in range(3):
        if i >= j:
            plt.subplot(3, 3, i*3 + j + 1)
            plt.scatter(inputs[:,i+1], inputs[:,j], s=2, c=categories)
            plt.xticks([])
            plt.yticks([])
        if i == 2:
            plt.xlabel(names[j], fontsize=6)
        if j == 0:
            plt.ylabel(names[i+1], fontsize=6)

import matplotlib.patches as mpatches

ax = plt.subplot(3, 3, 3)
scatter = ax.scatter([0,2,3], [10, 10, 10], c = [0,1,2])
plt.ylim([0,1])
plt.axis("off")


pop_a = mpatches.Patch(color='#440154', label='setosa')
pop_b = mpatches.Patch(color='#20918c', label='versicolor')
pop_c = mpatches.Patch(color='#fee724', label='virginica')

plt.legend(handles=[pop_a,pop_b, pop_c])

#print(list(lines))
#plt.ylim([0,1])
#plt.legend(handles = scatter.legend_elements(num=3))
#plt.legend([0,1,2], ["setosa", "versicolor", "virginica"])

plt.savefig("figurer/iris_oversikt.pdf")
#plt.show()

"""