import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn import datasets

# data on breast cancer
breast_cancer = datasets.load_breast_cancer()

df = pd.DataFrame(breast_cancer.data, columns=breast_cancer.feature_names)
print(df.head())
df.info()

print(df.corr())

print(df.corr().abs().nlargest(3, 'worst fractal dimension'))

plt.scatter(df['worst compactness'], df['mean fractal dimension'], marker='o')
plt.show()


fig = plt.figure(figsize=(18, 15))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df['worst compactness'],
           df['mean fractal dimension'],
           df['worst fractal dimension'],
           c='b')
plt.show()

