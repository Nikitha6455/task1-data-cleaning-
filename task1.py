import pandas as pd

# STEP 1: Load dataset
df = pd.read_csv("titanic.csv")

print("First 5 rows:")
print(df.head())

# STEP 2: Dataset info
print("\nDataset Info:")
print(df.info())

# STEP 3: Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# STEP 4: Handle missing values

# Fill age with mean
df['age'] = df['age'].fillna(df['age'].mean())

# Fill embarked with mode
df['embarked'] = df['embarked'].fillna(df['embarked'].mode()[0])

# STEP 5: Remove duplicates
df = df.drop_duplicates()

# STEP 6: Standardize text
df['sex'] = df['sex'].str.lower().str.strip()

# STEP 7: Fix column names
df.columns = df.columns.str.lower().str.replace(' ', '_')

# STEP 8: Convert types
df['age'] = df['age'].astype(int)

# STEP 9: Final check
print("\nCleaned Data Info:")
print(df.info())

# STEP 10: Save cleaned file
df.to_csv("cleaned_titanic.csv", index=False)

print("\n✅ Cleaning complete! File saved as cleaned_titanic.csv")