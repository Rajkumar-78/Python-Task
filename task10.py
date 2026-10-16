import pandas as pd
data = {
    "id": [1, 2, 3, 4, 5, 6, 7, 8],
    "name": ["Arun", "Priya", "Rahul", "Divya", "Karthik", "Meena", "Suresh", "Anitha"],
    "department": ["Sales", "HR", "IT", "IT", "Finance", "Sales", "IT", "HR"],
    "salary": [30000, 45000, 60000, 75000, 90000, 52000, 68000, 48000],
    "city": ["Chennai", "Chennai", "Bangalore", "Chennai", "Mumbai", "Bangalore", "Chennai", "Mumbai"]
}

df = pd.DataFrame(data)

df.to_csv("employees.csv", index=False)
df = pd.read_csv("employees.csv")

print("Chennai:", ", ".join(df.loc[df["city"] == "Chennai", "name"]))

high_salary = df[df["salary"] > 50000]
print("Salary above 50000:", len(high_salary), "employees")

it_employees = df[df["department"] == "IT"]
print("IT department:", ", ".join(it_employees["name"]))
