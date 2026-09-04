import streamlit as st
import pandas as pd
from numpy.random import default_rng as rng

st.title("My Web app by Streamlit")
st.header("_Streamlit_ is :blue[cool] :sunglasses:")

st.subheader("These subheaders have rotating dividers", divider=True)

amount = st.number_input(
    "Enter your amount",
    min_value=0.0
)

per = st.select_slider(
    "Select percentage discount of amount",
    options=[0, 5, 10, 15, 50]
)

# Button action
# if st.button("Calculate Discount"):
discount = amount - (amount * per / 100)
product_data = {
    "Previous amount": [
        f"{amount:.2f}"
    ],
    "After Discount": [
        f"{discount:.2f}"
    ],
}

st.table(product_data, border="horizontal")


st.success(f"Your discounted amount is ₹{discount:.2f}")


uploaded_file = st.file_uploader(
    "Choose an Excel file",
    type=["xlsx"]
)

if uploaded_file is not None:
    # Read Excel file
    df = pd.read_excel(uploaded_file)

    # Display as table
    st.subheader("Excel Data")
    st.dataframe(df)   # interactive table
    # st.table(df)     # static table


url = "data.xlsx"

df = pd.read_excel(url)
st.dataframe(df) 
chart_df = df[["district_name", "grand_total"]]

# Bar chart
st.bar_chart(
    chart_df,
    x="district_name",
    y="grand_total"
)



map_df = df[["Latitude", "Longitude"]]
map_df.columns = ["lat", "lon"]

st.map(map_df)