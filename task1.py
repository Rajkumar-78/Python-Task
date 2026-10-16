a = 12000
b = 12000.0
c= "sales report"
d = [12000, 0, 8500, 15000, -200, 9800]
e = {"sales": 30000}
f = {12000, 8500, 15000}
g  = (12000, 8500, 15000)
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))
print(f, type(f))
print(g, type(g))
sales = [12000, 0, 8500, 15000, -200, 9800]

total = 0

for sale in sales:
    if sale <= 0:
        print("Skipped invalid value:", sale)
        continue

    total = sale + total
    print("Added:", sale, "Total:", total)

    if total > 30000:
        print("Target reached. Stopped.")
        print("At:", total)
        break
    
          