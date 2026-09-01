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
st.bar_chart(list(sales.values()))