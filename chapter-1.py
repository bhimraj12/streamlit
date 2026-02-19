# def main():
#     print("Hello from streamlit!")


# if __name__ == "__main__":
#     main()

import streamlit as st
st.title("Hello from Streamlit!")
st.subheader("Subheader from Streamlit!")
st.text("Welcome to your first interactive Streamlit app!")
st.write("Choose your favorite color:")

color = st.selectbox("Select a color", ["Red", "Green", "Blue"])
st.write("You selected:", color)
st.write("You selected: {color} color".format(color=color))
st.write(f"You selected: {color} color")