import pandas as pd

df = pd.read_csv("students.csv")

print("Data:")
print(df)

print("\nFirst 5 rows:")
print(df.head())

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nInformation:")
df.info()

print("\nStatistics:")
print(df.describe())

print("\nMissing values:")
print(df.isnull().sum())

print("\nAverage Age:")
print(df["Age"].mean())

print("\nStudents by City:")
print(df["City"].value_counts())
