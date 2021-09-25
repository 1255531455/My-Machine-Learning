import pandas as pd
df = pd.read_csv("NaNDataset.csv")

print(df)

""" Check null """
print(df.isnull().sum())

# Replace with the mean of the column
df.B = df.B.fillna(df.B.mean())
print(df)

# Delete null lines
df = pd.read_csv("NaNDataset.csv")
df = df.dropna()
df = df.reset_index(drop=True)  # reset the index
print(df)

""" Delete duplicate lines """

df = pd.read_csv("NaNDataset.csv")

# Check duplicate lines
print(df.duplicated(keep='first'))
print(df[df.duplicated(keep='first')])

# Delete duplicate
df.drop_duplicates(keep='first', inplace=True)  # keep first and inplace=True means dataframe will change
print(df)

# Delete duplicate column
df.drop_duplicates(subset=['B', 'C'], keep='last', inplace=True)
print(df)
