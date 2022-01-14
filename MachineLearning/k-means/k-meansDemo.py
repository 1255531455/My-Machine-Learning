import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import metrics

df = pd.read_csv('BMX_G.csv')
print(df.shape)
print(df.isnull().sum())
df = df.dropna(subset=['bmxleg', 'bmxwaist'])
print(df.shape)

plt.scatter(df['bmxleg'], df['bmxwaist'], c='r', s=2)
plt.xlabel("Upper leeg length (cm)")
plt.ylabel("Waist Circumference (cm)")

# using sci-kit-learn
from sklearn.cluster import KMeans

k = 2
X = np.array(list(zip(df['bmxleg'], df['bmxwaist'])))

kmeans = KMeans(n_clusters=k)
kmeans = kmeans.fit(X)
labels = kmeans.predict(X)
centroids = kmeans.cluster_centers_

# map the labels to colors
c = ['b', 'r', 'y', 'g', 'c', 'm']
colors = [c[i] for i in labels]
plt.scatter(df['bmxleg'], df['bmxwaist'], c=colors, s=2)
plt.scatter(centroids[:, 0], centroids[:, 1], marker='*', s=100, c='black')
plt.show()

silhouette_avgs = []
min_k = 2

# try k from 2 to maximum number of labels
for k in range(min_k, 10):
    kmean = KMeans(n_clusters=k).fit(X)
    score = metrics.silhouette_score(X, kmean.labels_)
    print("Silhouette Coefficients for k =", k, "is", score)
    silhouette_avgs.append(score)

# the optimal k is the one with the highest average silhouette
Optimal_K = silhouette_avgs.index(max(silhouette_avgs)) + min_k
print("Optimal K is", Optimal_K)