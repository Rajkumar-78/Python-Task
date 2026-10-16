import pandas as pd
orders = pd.DataFrame({
    "order_id": [1, 2, 3, 4, 5],
    "customer_id": [101, 102, 103, 104, 105],
    "amount": [500, 1000, 1500, 2000, 2500]
})
customers = pd.DataFrame({
    "customer_id": [101, 102, 103, 105],
    "name": ["Arun", "Priya", "Rahul", "Divya"],
    "city": ["Chennai", "Mumbai", "Chennai", "Bangalore"]
})
inner_join = pd.merge(orders, customers, on="customer_id", how="inner")
print("Inner join rows:", len(inner_join), "(customer 104 dropped)")
left_join = pd.merge(customers, orders, on="customer_id", how="left")
no_orders = left_join[left_join["order_id"].isna()]
print("No orders:", "Divya" if no_orders.empty else ", ".join(no_orders["name"]))
outer_join = pd.merge(
    orders, customers, on="customer_id",
    how="outer", indicator=True
)
missing_customer = outer_join[outer_join["_merge"] == "left_only"]
print("Order without customer: customer_id",
      int(missing_customer.iloc[0]["customer_id"]))
