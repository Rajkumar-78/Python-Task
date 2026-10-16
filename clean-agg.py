import pandas as pd
data = {
    "order_id": [1, 2, 3, 3, 4, 5],
    "customer_id": [101, 102, 101, 101, 103, 104],
    "amount": [500, None, 700, 700, 300, 900]
}
df = pd.DataFrame(data)
df.to_csv("orders.csv", index=False)
df = pd.read_csv("orders.csv")
missing = df.isna().sum()
duplicates = df.duplicated().sum()
print(f"Missing: amount {missing['amount']} | Duplicates: {duplicates}")
df = df.drop_duplicates()
median_value = df["amount"].median()
df["amount"] = df["amount"].fillna(median_value)
print(f"Median used: {median_value:.1f}")
df["amount"] = pd.to_numeric(df["amount"])
df["order_id"] = df["order_id"].astype(str)
result = df.groupby("customer_id").agg(
    total=("amount", "sum"),
    orders=("order_id", "count")
)
print(result)