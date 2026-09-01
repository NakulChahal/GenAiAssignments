# Assignment 4: File handling

## Task 1:Write sales record to a file


```python
sales = [200,450,980,1500,3000]

f = open("sales_data.txt", "w")

for i, x in enumerate(sales):
    if i == len(sales) - 1:
        f.write(str(x))
    else:
        f.write(str(x) + ",\n")

f.close()

f = open("sales_data.txt", "r")

print(f.read())
f.close()
```

    200,
    450,
    980,
    1500,
    3000


## Task 2: read file n diff ways


```python
f = open("sales_data.txt", "r")

print(f.read())
f.close()

f = open("sales_data.txt", "r")

print("Read first line",f.readline())
f.close()

f = open("sales_data.txt", "r")

data = f.readlines()
numbers = [int(line.strip().replace(",", "")) for line in data]
print(numbers)
f.close()
```

    200,
    450,
    980,
    1500,
    3000
    Read first line 200,
    
    [200, 450, 980, 1500, 3000]


## Task 3: Append new lines


```python
new_list=[5000,2500,1700]
f = open("sales_data.txt", "a")

for i, x in enumerate(new_list):
    if i == len(new_list) - 1:
        f.write("\n" + str(x))
    else:
        f.write("\n" + str(x) + ",")
f.close()
f = open("sales_data.txt", "r")
print(f.read())
f.close()
f = open("sales_data.txt", "r")
data = f.readlines()
numbers = [line.strip().replace(",", "") for line in data]
print(numbers)
f.close()
```

    200,
    450,
    980,
    1500,
    3000
    5000,
    2500,
    1700
    5000,
    2500,
    1700
    [200, 450, 980, 1500, 3000, 5000, 2500, 1700, 5000, 2500, 1700]


## Task 4: Generate summary report


```python
f = open("sales_data.txt", "r")

print(f.read())
f.close()

f = open("sales_data.txt", "r")

data = f.readlines()
numbers = [int(line.strip().replace(",", "")) for line in data]
print(numbers)
cal=lambda x:sum(x)
print("Total sale:",cal(numbers))
heightest_sale=lambda x:max(x)
print("Heighest sale:",heightest_sale(numbers))
avg_sale=lambda x:(sum(x)/len(numbers))
print("Avg sale:",avg_sale(numbers))
f.close()
```

    200,
    450,
    980,
    1500,
    3000
    5000,
    2500,
    1700
    5000,
    2500,
    1700
    [200, 450, 980, 1500, 3000, 5000, 2500, 1700, 5000, 2500, 1700]
    Total sale: 24530
    Heighest sale: 5000
    Avg sale: 2230.0


## Task 5:Create product info file


```python
f=open("products.txt","w")
for i in range(3):
    product_name=input(f"Enter your product {i} Name: ")
    product_price=input(f"Enter your {product_name} Price: ")
    f.write(product_name + " | " + product_price + "\n")
f.close()

```


```python
f = open("products.txt", "r")

for line in f.readlines():
    name, price = line.strip().split("|")
    print(f"Product: {name.strip()}  Price: ₹{price.strip()}")
f.close()
```

    Product: mobile  Price: ₹30000
    Product: charger  Price: ₹1500
    Product: mouse  Price: ₹500


## Task 6: Read file safely


```python
file_name = input("Enter file name: ")
com_file_name=file_name+".txt"
try:
    f = open(com_file_name, "r")
    print(f.read())
    f.close()

except FileNotFoundError as e:
    print("File not found.Please check file name.", e)

```

    mobile | 30000
    charger | 1500
    mouse | 500
    



```python
import os

file_name = input("Enter file name: ")
com_file_name=file_name+".txt"
if os.path.exists(com_file_name):
    f = open(com_file_name, "r")
    print(f.read())
    f.close()
else:
    print("File does not exist.")
```

    mobile | 30000
    charger | 1500
    mouse | 500
    


## Task 7: Mini project


```python
prices = {
    "Mouse": 500,
    "Keyboard": 800,
    "Monitor": 7000,
    "Pendrive": 400,
    "Camera": 5000
}

discount = float(input("Enter discount percentage: "))

total_discounted = 0

# Write to file
with open("discount_report.txt", "w") as f:

    f.write("Product | Original Price | Discounted Price\n")
    f.write("-"*45 + "\n")

    for product, price in prices.items():

        discounted_price = price - (discount/100 * price)

        total_discounted += discounted_price

        f.write(f"{product} | {price} | {discounted_price}\n")

    # Summary
    avg_discounted = total_discounted / len(prices)

    f.write("\nSummary\n")
    f.write(f"Total Items: {len(prices)}\n")
    f.write(f"Average Discounted Price: {avg_discounted}\n")

# Read and print file
with open("discount_report.txt", "r") as f:
    print(f.read())
```

    Product | Original Price | Discounted Price
    ---------------------------------------------
    Mouse | 500 | 400.0
    Keyboard | 800 | 640.0
    Monitor | 7000 | 5600.0
    Pendrive | 400 | 320.0
    Camera | 5000 | 4000.0
    
    Summary
    Total Items: 5
    Average Discounted Price: 2192.0
    

