import csv
import json

names = ["Arun", "Priya", "Rahul", "Divya", "Karthik"]

# Write and read names
with open("names.txt", "w") as file:
    for name in names:
        file.write(name + "\n")

with open("names.txt", "r") as file:
    for number, name in enumerate(file, start=1):
        if number <= 2:
            print(name.strip())

# Create students.csv
students = [
    {"name": "Arun", "marks": 55},
    {"name": "Priya", "marks": 60},
    {"name": "Rahul", "marks": 72},
    {"name": "Divya", "marks": 88},
    {"name": "Karthik", "marks": 45}
]

with open("students.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "marks"])
    writer.writeheader()
    writer.writerows(students)

# Read CSV
with open("students.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    result = [
        f"{s['name']} {s['marks']}"
        for s in reader if int(s["marks"]) > 60
    ]

print("Above 60: " + " ".join(result))

# Write and read JSON
with open("students.json", "w") as file:
    json.dump(students, file, indent=2)

with open("students.json", "r") as file:
    data = json.load(file)

# Handle missing file
try:
    with open("missing.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Missing.txt -> File Not Found")
