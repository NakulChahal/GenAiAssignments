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
    st.write(f"**Price:** ₹{price:.2f}")