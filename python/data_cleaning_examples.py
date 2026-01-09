import pandas as pd

# Load data
df = pd.read_csv("data.csv")

# Remove duplicates
df.drop_duplicates(inplace=True)

# Handle missing values
df.fillna(0, inplace=True)

# Feature engineering
df["revenue"] = df["quantity"] * df["price"]

# Preview cleaned data
print(df.head())
