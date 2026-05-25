# Assignment 3 : Functions

## Task 1- Basic function: price after discount


```python
# 1,2 apply discount fn
def apply_discount(price,dis_percentage=5):
    if dis_percentage > 60:
        return "exceed discount limit,limit should be till 60 %."
    price_after_dis= int(price - price * dis_percentage/100)
    return price_after_dis
```


```python
 # test with given fn
apply_discount(1000,70)

```




    'exceed discount limit,limit should be till 60 %.'




```python
 # test with  
apply_discount(500)
```




    475



## Task 2: recursive function: factorial utility


```python
def factorial(n):
    fact=1
    if n == 0 or n == 1:
     return 1
    elif n < 0:
        return "Less then 0 is not allowed for this fun.."
    for num in range(1,n+1):
        fact =fact * num
    
    return fact
```


```python
print(factorial(5))
print(factorial(0))
print(factorial(-3))
```

    120
    1
    Less then 0 is not allowed for this fun..


## Task 3 :Lambda function:GST cal..


```python
def calculate_gst(price):
    gst=lambda price : price +(0.18 * price)
    return gst(price)
```


```python
print(calculate_gst(100))
calculate_gst(350)
```

    118.0





    413.0



## price after gst and discount


```python
def discount(price,dis):
    gst=lambda price : price + (0.18 * price)-(dis/100 * price)
    return gst(price)
print(discount(400,5))
```

    452.0


## Task 4: Using map()


```python
def cal_gst(prices,gst):
    gst_price=list(
        map(lambda prices:prices + (gst /100 * prices),prices)
        )
    return gst_price
```


```python
prices=[100,250,400,50,1200]
print(f"original prices list:{prices}")
print("Price after GST.")
print(cal_gst(prices,18))
```

    original prices list:[100, 250, 400, 50, 1200]
    Price after GST.
    [118.0, 295.0, 472.0, 59.0, 1416.0]


## Task 5: Using filter


```python
prices=[100,250,400,50,1200,2000,850]
def grater_value(prices):
    grater_list=list(
        filter(lambda x: x > 500,prices)
        )
    return grater_list

def less_equal_values(prices):
    less_lq=list(
        filter(lambda x: x <= 500 ,prices)
    )    
    return less_lq
```


```python
print("Grater values then 500:",grater_value(prices))
print("Less and equal to 500 values in list:",less_equal_values(prices))
```

    Grater values then 500: [1200, 2000, 850]
    Less and equal to 500 values in list: [100, 250, 400, 50]


## Task 6 : combined utility fn


```python
def process_prices(prices):
    discount_price_list=list(
        map(lambda x:x -(10/100 * x),prices)
    )
    price_above_300=list(
        filter(lambda x : x > 300,discount_price_list)
    )
    return discount_price_list,price_above_300
```


```python
print("discount price list:",process_prices([100,500,900,50,750])[0])
print("grater then 300 price list:",process_prices([100,500,900,50,750])[1])
```

    discount price list: [90.0, 450.0, 810.0, 45.0, 675.0]
    grater then 300 price list: [450.0, 810.0, 675.0]


## Task 7: Mini problem


```python
list_price=[100,200,300,400,345,500,600]
def add_price(list_price):
    price_list=[]
    total_price = 0
    for x in list_price:
        price_list.append(x)
        total_price+=x
    average_price=total_price/len(list_price)
    max_price=max(list_price)
    return price_list,average_price,max_price
```


```python
print("List of prices:", add_price(list_price)[0])
print("Average price:", add_price(list_price)[1])
print("Max price:", add_price(list_price)[2])
```

    List of prices: [100, 200, 300, 400, 345, 500, 600]
    Average price: 349.2857142857143
    Max price: 600

