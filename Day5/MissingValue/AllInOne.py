import pandas as pd

# Read CSV
df = pd.read_csv("Stud.csv")

print("Original Dataset:")
print(df)

# Step 33 - Detect missing values
print("\nMissing Values:")
print(df.isnull())

# Step 34 - Count missing values
print("\nCount of Missing Values:")
print(df.isnull().sum())

# Step 35 - Remove rows with missing values
# print("\nAfter Removing Missing Values:")
# print(df.dropna())

# Step 36 - Fill missing Marks with average
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

print("\nAfter Filling Missing Marks:")
print(df)

# Step 37 - Fill missing Salary with average
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

print("\nAfter Filling Missing Salary:")
print(df)

# Step 38 - Fill missing Department
df["Department"] = df["Department"].fillna("Unknown")

print("\nAfter Filling Missing Department:")
print(df)

# Step 39 - Save cleaned dataset
df.to_csv("cleaned_students.csv", index=False)

print("\nCleaned dataset saved successfully!")