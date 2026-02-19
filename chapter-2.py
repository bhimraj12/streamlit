import streamlit as st

st.title("Chai Maker App")

if st.button("Make Chai"):
    st.success("Chai is being brewed!")

addMasala = st.checkbox("Add Masala")

if addMasala:
    st.success("Masala added!")
else:
    st.warning("Masala not added!")


teaType = st.radio("Pick your favorite tea", ["Black", "Green", "Oolong", "White"])

st.write(f"You selected {teaType} tea!")

flavour = st.selectbox("Pick your favorite tea flavour", ["Adrak", "Kesar", "Lemon", "Tulsi"])

st.write(f"You selected {flavour} tea!")

sugar = st.slider("How much sugar?", 0, 100, 20)

st.write(f"You selected {sugar} grams of sugar!")

quantity = st.number_input("How many cups?", 1, 10)

st.write(f"You selected {quantity} cups!")

name = st.text_input("Enter your name", placeholder="Enter name")

if name:
    st.write(f"Welcome, {name}! Your Chai is on its way!")

dob = st.date_input("Enter your date of birth")

st.write(f"You were born on {dob}")