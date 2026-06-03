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
    st.success(f"Discounted Price: ₹{discounted_price:.2f}")