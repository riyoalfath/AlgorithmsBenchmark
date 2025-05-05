import pandas as pd

# Load the original data
df = pd.read_csv("customer_shopping_data.csv")

# Reduce to 100, 1000, and 10,000 rows (random samples)
df_100 = df.sample(n=100, random_state=42)
df_1000 = df.sample(n=1000, random_state=42)
df_10000 = df.sample(n=10000, random_state=42)

# Optional: Save to CSV
df_100.to_csv("customer_shopping_data_100.csv", index=False)
df_1000.to_csv("customer_shopping_data_1000.csv", index=False)
df_10000.to_csv("customer_shopping_data_10000.csv", index=False)