import pandas as pd

df = pd.read_csv("../Dataset/raw_crime_data.csv")


print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())


print("\nDataset Information:")
df.info()