# Task 1: Craete numpy array


```python
# 1D array
import numpy as np
od=np.arange(1,10)
print(od)
print(od.dtype)
```

    [1 2 3 4 5 6 7 8 9]
    <class 'numpy.ndarray'>
    int64



```python
# 2D array
tD=np.arange(1,10).reshape(3,3)
print(tD)
print(tD.dtype)
```

    [[1 2 3]
     [4 5 6]
     [7 8 9]]
    int64



```python
# list
listArray=[10,20,30,40,50]
arr=np.array(listArray)
print(arr)
print(arr.dtype)
```

    [10 20 30 40 50]
    int64


## Task 2:imp maths operations


```python
A=np.array([10,20,30,40])
B=np.array([1,2,3,4])
# addition A+B
print(A+B)

# subtarction A-B
print(A-B)
# Multiplication A * B
print(A*B)
# Divide A/B
print(A/B)
# Power of A**2
print(A**2)

# Extra
# add()
print(np.add(A,B))

# subtract()
print(np.subtract(A,B))
```

    [11 22 33 44]
    [ 9 18 27 36]
    [ 10  40  90 160]
    [10. 10. 10. 10.]
    [ 100  400  900 1600]
    [11 22 33 44]
    [ 9 18 27 36]


## Task 3:Imp Numpy maths formulas


```python
values=np.array([2,4,6,8,10])
print(np.sqrt(values)) # sqrt of each element
print(np.exp(values)) # exponential of each element
print(np.log(values)) # log of each element
print(np.sum(values)) # sum of each element
print(np.cumulative_sum(values)) # commulative sum of each element


```

    [1.41421356 2.         2.44948974 2.82842712 3.16227766]
    [7.38905610e+00 5.45981500e+01 4.03428793e+02 2.98095799e+03
     2.20264658e+04]
    [0.69314718 1.38629436 1.79175947 2.07944154 2.30258509]
    30
    [ 2  6 12 20 30]


## Task 4:Aggregation Operations


```python
# 2 D aaray

data=np.array([[10,20,30],
                [40,50,60],
                [70,80,90]])
row_sum = np.sum(data, axis=1)
# row wise sum()
print(row_sum)

# column wise sum()
col_sum = np.sum(data, axis=(0))
print(col_sum)

# min value
print(np.min(data))

# max value
print(np.max(data))

# overall mean()
print(np.mean(data))

```

    [ 60 150 240]
    [120 150 180]
    10
    90
    50.0


## Task 5:statistical Ops (core focus)


```python
marks=np.array([78,85,90,66,72,88,96,60]) # array list
# mean()
print(np.mean(marks))

# median()
print(np.median(marks))

# variance()
print(np.var(marks))

# standard Deviation
print(np.std(marks))

# min()
print(np.min(marks))

# max()
print(np.max(marks))

# range (min() - max())
range_value = np.max(marks) - np.min(marks)

print(range_value)
```

    79.375
    81.5
    138.234375
    11.757311554943163
    60
    96
    36


## Task 6: Percentile & sorting


```python
marks=np.array([78,85,90,66,72,88,96,60]) # array list
print(np.sort(marks))

# 25th percentile
p25 = np.percentile(marks, 25)

print(p25)

# 50th percentile
p50 = np.percentile(marks, 50)

print(p50)

# 75th percentile
p75 = np.percentile(marks, 75)

print(p75)

# avg marks
avg_marks = np.mean(marks)

# count above avg marks
count_above_avg = np.sum(marks > avg_marks)

print("Average Marks:", avg_marks)
print("Students Above Average:", count_above_avg)
```

    [60 66 72 78 85 88 90 96]
    70.5
    81.5
    88.5
    Average Marks: 79.375
    Students Above Average: 4


## Task 7:Mini use case: sales analysis


```python
sales=np.array([1200,1500,900,2000,1800,1700,1600])
# total weekly sale
print(np.sum(sales))
# avg daily sale
print(np.average(sales))
# heighest daily sale
print(np.max(sales))
# lowest daily sale
print(np.min(sales))

# standard deviation daily sale
print(np.std(sales))

# sales were above avg
# avg sales
avg_sales = np.mean(sales)
print("Avg sale: ",avg_sales)
count_above_avg_sale=np.sum(sales > avg_sales)
print("Count avg sales: ",count_above_avg_sale)


```

    10700
    1528.5714285714287
    2000
    900
    345.2298849598449
    Avg sale:  1528.5714285714287
    Count avg sales:  4

