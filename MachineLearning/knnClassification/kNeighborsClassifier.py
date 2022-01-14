import pandas as pd
import numpy as np
from sklearn import svm, datasets
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

iris = datasets.load_iris()

X = iris.data[:, :2]  # take the first two features
y = iris.target

# 当k值越高边界越平滑，可能出现欠拟合；k值越低可能出现过度拟合
k = 13
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X, y)
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

z = knn.predict(np.c_[xx.ravel(), yy.ravel()])

# draw the result using a color plot
z = z.reshape(xx.shape)
plt.contourf(xx, yy, z, cmap=plt.cm.Accent, alpha=0.8)

# plot the training points
colors = ['red', 'green', 'blue']
for color, i, target in zip(colors, [0, 1, 2], iris.target_names):
    plt.scatter(X[y == i, 0], X[y == i, 1], color=color, label=target)
plt.xlabel("Sepal length")
plt.ylabel("Sepal width")
plt.title("f'KNN (k={k})'")
plt.legend(loc='best', shadow=False, scatterpoints=1)

predictions = knn.predict(X)

print(np.unique(predictions, return_counts=True))

# 参数k的调整
from sklearn.model_selection import cross_val_score

# holds the cv scores
cv_scores = []

# use all feature
X = iris.data[:, :4]
y = iris.target

# number of folds
folds = 10

# creating odd list of K for KNN
ks = list(range(1, int(len(X) * ((folds - 1)/folds))))

# remove all multiples of 3
ks = [k for k in ks if k % 3 != 0]

# perform k-fold cross validation
for k in ks:
    knn = KNeighborsClassifier(n_neighbors=k)

    # performs cross-validation and returns the average accuracy
    scores = cross_val_score(knn, X, y, cv=folds, scoring='accuracy')
    mean = scores.mean()
    cv_scores.append(mean)
    print(k, mean)

# calculate misclassification error for each k
MSE = [1 - x for x in cv_scores]

# determining best k (min. MSE)
optimal_k = ks[MSE.index(min(MSE))]
print(f"The optimal number of neighbors is {optimal_k}")

# plot MSE vs k
plt.figure(2)
plt.plot(ks, MSE)
plt.xlabel('Number of Neighbors k')
plt.ylabel('Misclassification Error')
plt.show()
