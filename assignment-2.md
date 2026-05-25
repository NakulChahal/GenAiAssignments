# Assignment 2:Python -control flow

## Task 1: Discount rule (if/elif/else)


```python
# insert value from user
order_amount = int(input("Enter Amount for order: "))

print(f"Your amount is {order_amount}")

if order_amount >= 2000:
    print("Discount of this product is 15%.")
elif order_amount >= 1500 and order_amount < 2000:
    print("Discount of this product is 10%.")
elif order_amount >= 1000 and order_amount < 1500:
    print("Discount of this product is 7%.")
else:
    print("Discount of this product is 0%.")

# Extra for Task 1 add 5% tax with final amount
final_amount = order_amount + (order_amount * 5 / 100)

print("Final Amount:", final_amount)
```

    Your amount is 65756
    Discount of this product is 15%.
    Final Amount: 69043.8


## Task 2: Process Multiple order (for loop)


```python
     ## list of orders
    
order_amount=[1200,2500,800,1750,3000]
final_amount_list =[]
discount_amount_list =[]
total_revenue=0
for list_order in order_amount:
    print(f"your amount is {list_order}")
    if list_order >= 2000:
        discount_amount_list.append((list_order - (list_order * 15 / 100)))
        total_revenue+=(list_order - (list_order * 15 / 100))
        print("Discount of this product is 15%.")
    elif list_order >= 1500 and list_order < 2000:
        discount_amount_list.append(list_order - (list_order * 10 / 100))
        total_revenue+=(list_order - (list_order * 10 / 100))
        print("Discount of this product is 10%.")    
    elif list_order >= 1000 and list_order < 1500:
        discount_amount_list.append(list_order - (list_order * 7 / 100))
        total_revenue+=(list_order - (list_order * 7 / 100))
        print("Discount of this product is 7%.")  
    else:
        print("Discount of this product is 0%.")

        # Extra for Task 1 add 5% tax with final amount

    final_amount_list.append(list_order + (list_order * 5 / 100))

    # total final list
    print("Final Amount List:", final_amount_list)
    # total Revenue generate by sell.
    print("Final Revenue List:", total_revenue)
    # total discount list
    print("Final Discount Amount List:", discount_amount_list)

```

    your amount is 1200
    Discount of this product is 7%.
    your amount is 2500
    Discount of this product is 15%.
    your amount is 800
    Discount of this product is 0%.
    your amount is 1750
    Discount of this product is 10%.
    your amount is 3000
    Discount of this product is 15%.
    Final Amount List: [1260.0, 2625.0, 840.0, 1837.5, 3150.0]
    Final Revenue List: 7366.0
    Final Discount Amount List: [1116.0, 2125.0, 1575.0, 2550.0]


# Task 3: User menu (while loop + break/continue)


```python

orders = []

while True:

    print("\n---- MENU ----")
    print("1 - Add Order Amount")
    print("2 - Show All Orders")
    print("q - Quit")

    choice = input("Enter your choice: ")

    # Add order
    if choice == "1":

            order_amount = int(input("Enter Amount for order: "))

            # Apply discount
            if order_amount >= 2000:
                discount = 15

            elif order_amount >= 1500:
                discount = 10

            elif order_amount >= 1000:
                discount = 7

            else:
                discount = 0

            # Discount calculation
            discount_amount = order_amount * discount / 100
            final_amount = order_amount - discount_amount

            # Add 5% tax
            final_amount = final_amount + (final_amount * 5 / 100)

            # Store in list
            orders.append(final_amount)

            print("Order added successfully.")
            print("Final Amount:", final_amount)

       

    # Show all orders
    elif choice == "2":

        print("\nAll Orders:")
        total = 0

        for order in orders:
            print(order)
            total += order

        print("Total Amount:", total)

    # Quit
    elif choice == "q":
        print("Exiting program...")
        break

    # Invalid input
    else:
        print("Invalid choice. Try again.")
        continue
```

    
    ---- MENU ----
    1 - Add Order Amount
    2 - Show All Orders
    q - Quit
    Invalid choice. Try again.
    
    ---- MENU ----
    1 - Add Order Amount
    2 - Show All Orders
    q - Quit
    Invalid choice. Try again.
    
    ---- MENU ----
    1 - Add Order Amount
    2 - Show All Orders
    q - Quit
    Invalid choice. Try again.
    
    ---- MENU ----
    1 - Add Order Amount
    2 - Show All Orders
    q - Quit
    Invalid choice. Try again.
    
    ---- MENU ----
    1 - Add Order Amount
    2 - Show All Orders
    q - Quit
    Exiting program...

