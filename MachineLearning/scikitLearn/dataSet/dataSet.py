import pandas as pd
from sklearn import datasets
from matplotlib import pyplot as plt
from sklearn.datasets import make_regression
from sklearn.datasets import make_blobs
from sklearn.datasets import make_circles
import numpy as np

iris = datasets.load_iris()

print(iris.DESCR)
print(iris.data)
print(iris.feature_names)

df = pd.DataFrame(iris.data)
print(df.head())

# data on breast cancer
breast_cancer = datasets.load_breast_cancer()

# data on diabetes
diabetes = datasets.load_diabetes()

# dataset of 1797 8x8 images of hand-writen digits
digits = datasets.load_digits()

print(breast_cancer.data)

# 使用Kaggle数据集

# 使用UCI机器学习存储库

# 生成自己的数据集

# 线性分布的数据集
X, y = make_regression(n_samples=100, n_features=1, noise=5.4)
plt.scatter(X, y)
plt.show()

# 集群的数据集
X, y = make_blobs(500, centers=3)
rgb = np.array(['r', 'g', 'b'])
plt.scatter(X[:, 0], X[:, 1], color=rgb[y])
plt.show()

# 以循环方式分布的群集数据集
X, y = make_circles(n_samples=100, noise=0.09)
plt.scatter(X[:, 0], X[:, 1], color=rgb[y])
plt.show()

