import pandas as pd
import numpy as np

""" Tukey Fences """


def outliers_iqr(data):
    q1, q3 = np.percentile(data, [25, 75])
    iqr = q3 - q1
    lower_bound = q1 - (iqr * 1.5)
    upper_bound = q3 + (iqr * 1.5)
    return np.where((data > upper_bound) | (data < lower_bound))  # return the outliers index


df = pd.read_csv("galton.csv")
print(df.head())

# find the outliers
print("Outliers using outliers_iqr()")
print("================================")
for i in outliers_iqr(df.height)[0]:
    print(df[i:i + 1])

""" Z-score """


def outliers_z_score(data):
    threshould = 3
    mean = np.mean(data)
    std = np.std(data)
    z_scores = [(y - mean) / std for y in data]
    return np.where(np.abs(z_scores) > threshould)


# use Z-score
print("Outliers using outliers_z_score()")
print("================================")
for i in outliers_z_score(df.height)[0]:
    print(df[i:i+1])
