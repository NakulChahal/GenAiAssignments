# Task 1: safe division Utility

## 1 takes two inputs:

## 2 try-except


```python
try:
    numerator = int(input("Enter Numerator: "))
    denominator = int(input("Enter Denominator: "))

    result = numerator / denominator
    print("Result:", result)

except ValueError as e:
    print("Not a number!", e)

except ZeroDivisionError as e1:
    print("Denominator is Zero", e1)
finally:
    print("Operation Complete")
```

    Result: 66.66666666666667
    Operation Complete


## Task 2: Bill calculator with error handling


```python
prices = [120,350,'abc',500,-200,800]
total = 0

for x in prices:
    try:
        if x < 0:
            raise ValueError("Negative price not allowed")

        total += x

    except TypeError as e:
        print("Not a number:", e)

    except ValueError as e:
        print(e)

print("Total =", total)
```

    Not a number: '<' not supported between instances of 'str' and 'int'
    Negative price not allowed
    Total = 1770


## Task 3 : custom exception: Age validate


```python
def check_age(age):
    if age < 1 or age > 120:
        raise ValueError("Age should be between 1-120")
    return age

try:
    age_user=int(input("Enter your age:"))
    print(check_age(age_user))
except ValueError  as e:
    print("Age is not a Number",e)
```

    3


## Task 4: file rad with exception handle


```python
try:
    file_name = input("Enter a file name: ")

    with open(file_name + ".txt", "r") as f:
        for i in range(3):
            print(f.readline(), end="")

except FileNotFoundError as e:
    print("File not found:", e)

except PermissionError as e:
    print("Permission denied:", e)
finally:
    print("File operation attempted")
```

    my name is nakul.
    i am a software developer.
    i am trying to learn gen ai.
    File operation attempted


## Task 5: Mini program 


```python
cart = []
print("Enter q for Exit")

amount = input("Enter Price list separated with comma(,): ")

if amount == 'q':
    exit()
else:
    values = amount.split(",")

    for x in values:
        try:
            num = float(x)

            if num < 0:
                raise ValueError("Negative Value is not allowed")

            cart.append(num)

        except ValueError as e:
            print(f"Invalid value: {x} -> {e}")

print("Total Items: ",len(cart))
print("Total Bill: ",sum(cart))
```

    Enter q for Exit
    Invalid value: -6 -> Negative Value is not allowed
    Invalid value: -7 -> Negative Value is not allowed
    Total Items:  5
    Total Bill:  15.0

