import streamlit as st
import pandas as pd

st.title("Chai Sales Dashboard")

file = st.file_uploader("Upload a CSV file", type=["csv"])

if file:
    df = pd.read_csv(file)
    st.subheader("Data Preview")
    st.dataframe(df)

if file:
    st.subheader("Data Analysis")
    st.write(df.describe())

if file:
    cities = df["City"].unique()
    selectedCity = st.selectbox("Select a city", cities)
    FilteredData = df[df["City"] == selectedCity]
    st.dataframe(FilteredData)