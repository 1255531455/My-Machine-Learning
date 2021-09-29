import pandas as pd
import numpy as np
from sklearn import svm, datasets
import matplotlib.pyplot as plt

iris = datasets.load_iris()

X = iris.data[:, :2]  # take the first two features
y = iris.target

# plot the points
colors = ['red', 'green', 'blue']
for color, i, target in zip(colors, [0, 1, 2], iris.target_names):
    plt.scatter(X[y == i, 0], X[y == i, 1], color=color, label=target)

plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.legend(loc='best', shadow=False, scatterpoints=1)

plt.title('Scatter plot of Sepal width against')

C = 1  # SVM regularization parameter
clf = svm.SVC(kernel='linear', gamma='auto', C=C).fit(X, y)    # kernel = linear or rbf    # C控制着边界的光滑性，gamma确定点是否过度拟合
title = 'SVC with linear kernel'

# min and max for the first feature
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1

# min and max for the second feature
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1

# step size in the mesh
h = (x_max / x_min) / 100

# make predictions for each of the points in xx,yy
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))

z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

# draw the result using a color plot
z = z.reshape(xx.shape)
plt.contourf(xx, yy, z, cmap=plt.cm.Accent, alpha=0.8)

plt.show()

