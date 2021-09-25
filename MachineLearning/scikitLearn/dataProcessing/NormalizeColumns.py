import pandas as pd
from sklearn import preprocessing

df = pd.read_csv("NormalizeColumns.csv")
x = df.values.astype(float)

min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(x)
df = pd.DataFrame(x_scaled, columns=df.columns)
print(df)


