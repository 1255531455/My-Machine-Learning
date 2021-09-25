import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()

# copy from dataset into a 2-d list
X = []
for target in range(2):     # target means is_get_cancer
    X.append([[], [], []])
    for i in range(len(cancer.data)):
        if cancer.target[i] == target:
            print(cancer.target[i])
            X[target][0].append(cancer.data[i][0])  # x:mean radius
            X[target][1].append(cancer.data[i][1])  # y:mean texture
            X[target][2].append(cancer.data[i][2])
colours = ("r", "b")

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
for target in range(2):
    ax.scatter(X[target][0],
               X[target][1],
               X[target][2],
               c=colours[target])
ax.set_xlabel("mean radius")
ax.set_ylabel("mean texture")
ax.set_zlabel("mean perimeter")
plt.show()



