# Task 1: basic class and obj. creation


```python
class Product:
    def __init__(self,name,price,category) :
        self.name=name
        self.price=price
        self.category=category

    def get_info(self):
            print(f"Name :{self.name} ,Price: {self.price} ,Category : {self.category}")
            
    def calculate_discount(self, percent):
        discount = self.price * percent / 100
        return self.price - discount

p=Product("Mobile",100000,"Electronic")
details=p.get_info()
discount=Product("Mobile",100000,"Electronic")
final_dis=discount.calculate_discount(10)
print(f"Discount Price: {final_dis}")

        
```

## Task 2: constructor and encapsulation


```python
class Product:
    def __init__(self,name,price,category) :
        self.name=name
        self._price=price
        self.category=category
    def get_price(self):
        return self._price

    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
            print("Price updated successfully")
        else:
            print("Invalid price")
        return self.__price


p=Product("Mobile",100000,"Electronic")
s=Product("Mobile",100000,"Electronic")

p.get_price()
s.set_price(150000)

```

    Price updated successfully





    150000



## Task 3 : Inheritance


```python
class Product:
    def __init__(self,name,price,category) :
        self.name=name
        self.price=price
        self.category=category

    def get_info(self):
            return f"Name: {self.name}, Price: {self.price}, Category: {self.category}"

class ElectronicProduct(Product):

    def __init__(self, name, price, category, warranty_years):
        super().__init__(name, price, category)    
        self.warranty_years = warranty_years

    def get_info(self):      # Method Overriding
        return f"{super().get_info()}, Warranty: {self.warranty_years}"


e1 = ElectronicProduct(
    "Laptop",
    80000,
    "Electronics",
    2
)

print(e1.get_info())
```

    Name: Laptop, Price: 80000, Category: Electronics, Warranty: 2


## Task 4:Poltmorphisam


```python
class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def get_info(self):
        return f"Name: {self.name}, Price: {self.price}, Category: {self.category}"


class Laptop(Product):

    def get_info(self):      # Override
        return f"Laptop -> {self.name} | Price: ₹{self.price} | Category: {self.category}"


class Mobile(Product):

    def get_info(self):      # Override
        return f"Mobile -> {self.name} | Price: ₹{self.price} | Category: {self.category}"


# Objects
l = Laptop("Apple MacBook", 150000, "Laptop")
m = Mobile("Samsung S25", 100000, "Mobile")

# Polymorphism loop
products = [l, m]

for item in products:
    print(item.get_info())
```

    Laptop -> Apple MacBook | Price: ₹150000 | Category: Laptop
    Mobile -> Samsung S25 | Price: ₹100000 | Category: Mobile


## Task 5: Abstraction


```python
from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def process_payment(self, amount):
        pass


class CreditCard(Payment):

    def process_payment(self, amount):
        print(f"Paid {amount} using Credit Card")


class UPI(Payment):

    def process_payment(self, amount):
        print(f"Paid {amount} using UPI")


c = CreditCard()
u = UPI()

c.process_payment(500)
u.process_payment(1000)
```

    Paid 500 using Credit Card
    Paid 1000 using UPI


## Task 6: Magic Methods & Operator Overloading


```python
class Product:

    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    # Magic Method
    def __str__(self):
        return f"Product({self.name}, {self.price}, {self.category})"

    # Operator Overloading
    def __add__(self, other):
        return self.price + other.price


# Create objects
p1 = Product("Laptop", 80000, "Electronics")
p2 = Product("Mobile", 30000, "Electronics")

# __str__
print(p1)

# __add__
total_price = p1 + p2
print("Combined Price:", total_price)
```

    Product(Laptop, 80000, Electronics)
    Combined Price: 110000


## Task 7: Mini Project – Simple Inventory System


```python
class Product:

    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"Product({self.name}, {self.price}, {self.category})"

    def __add__(self, other):
        return self.price + other.price


class Inventory:

    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)

    def get_total_value(self):
        total = 0
        for product in self.products:
            total += product.price
        return total

    def show_all_products(self):
        print("Products List:")
        for product in self.products:
            print(product)


class Store:

    def __init__(self, store_name):
        self.store_name = store_name
        self.inventory = Inventory()

    def add_new_product(self, name, price, category):
        product = Product(name, price, category)
        self.inventory.add_product(product)

    def show_summary(self):
        print(f"Store: {self.store_name}")
        print("Total Products:", len(self.inventory.products))
        print("Total Inventory Value:", self.inventory.get_total_value())


# -------- Testing --------

# 1. Create Store
store = Store("Nakul Electronics")

# 2. Add 3 Products
store.add_new_product("Laptop", 80000, "Electronics")
store.add_new_product("Mobile", 30000, "Electronics")
store.add_new_product("Headphone", 5000, "Accessories")

# 3. Show Products
store.inventory.show_all_products()

# 4. Show Summary
store.show_summary()

# 5. Use __add__
p1 = store.inventory.products[0]
p2 = store.inventory.products[1]

print("Combined Price:", p1 + p2)
```

    Products List:
    Product(Laptop, 80000, Electronics)
    Product(Mobile, 30000, Electronics)
    Product(Headphone, 5000, Accessories)
    Store: Nakul Electronics
    Total Products: 3
    Total Inventory Value: 115000
    Combined Price: 110000

