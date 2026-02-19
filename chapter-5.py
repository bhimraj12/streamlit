import streamlit as st
import requests as req
st.title("Live currency converter")
amount = st.number_input("Enter the amount in INR", min_value=1, max_value=1000000, step=1)

targetCurrency = st.selectbox("Select the currency to convert", ["USD", "EUR", "GBP", "AUD", "CAD", "JPY"])

if st.button("Convert"):
    url = f"https://api.exchangerate-api.com/v4/latest/INR"
    response = req.get(url)

    if response.status_code == 200:
        data = response.json()
        rate = data["rates"][targetCurrency]
        convertedAmount = amount * rate
        st.write(f"{amount} INR = {convertedAmount:.2f} {targetCurrency}")
    else:
        st.write(f"Failed to convert currency. Status code: {response.status_code}")
 