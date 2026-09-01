```python
#Task 1:
import streamlit as st

st.title("Welcome to Streamlit!")

name = st.text_input("Enter your name")

if st.button("Greet Me"):
    st.write(f"Hello ,{name}")```


```python 
#task 2:
import streamlit as st
import pandas as pd

st.title("Welcome to Streamlit Calculator!")

# Product price input
product = st.number_input("Enter Product Price", min_value=0.0)

# Slider 0–50%
discount = st.slider("Select Discount %", 0, 50, 0)

# Button
if st.button("Calculate Discounted Price"):

    discounted_price = product - (product * discount / 100)

    # Create table
    data = pd.DataFrame({
    "Before Discount": [f"₹{product:.2f}"],
    "After Discount": [f"₹{discounted_price:.2f}"]
    })

    st.table(data)
    st.success(f"Discounted Price: ₹{discounted_price:.2f}")```


```python
# Task 3:
import streamlit as st

st.title("Product Management System")

# Sidebar Inputs
st.sidebar.header("Add Product")

product_name = st.sidebar.text_input("Product Name")

category = st.sidebar.selectbox(
    "Category",
    ["Electronics", "Clothing", "Books", "Food", "Sports"]
)

price = st.sidebar.number_input(
    "Price",
    min_value=0.0,
    format="%.2f"
)

# Sidebar Button
if st.sidebar.button("Add Product"):

    st.success("Product Added Successfully!")

    st.subheader("Product Details")

    st.write(f"**Product Name:** {product_name}")
    st.write(f"**Category:** {category}")
    st.write(f"**Price:** ₹{price:.2f}")```


```python
# Task 4 :
import streamlit as st

# Title + Description
st.title("Sales Dashboard")
st.write("View monthly sales data using a dropdown and chart.")

# Months list
months = ["January", "February", "March", "April"]

# Sales dictionary
sales = {
    "January": 1200,
    "February": 1500,
    "March": 900,
    "April": 2000
}

# Selectbox
selected_month = st.selectbox("Select Month", months)

# Display selected month's sales
st.metric(
    label=f"{selected_month} Sales",
    value=f"₹{sales[selected_month]}"
)

# Bar Chart
st.subheader("Monthly Sales Chart")
st.bar_chart(list(sales.values()))```


🌐 Website: [Erapse](https://erapse.com)

For more information, visit the [Erapse Official Website](https://erapse.com).

This project is powered by [Erapse](https://erapse.com).

Useful financial tools:
- [EMI Calculator](https://erapse.com/emi.html)
- [SIP Calculator](https://erapse.com/sip.html)
- [GST Calculator](https://erapse.com/gst.html)
