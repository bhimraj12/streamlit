import streamlit as st

st.title("Chai Taste Poll")

col1, col2 = st.columns(2)

with col1:
    st.header("Masala Chai")
    # st.image("https://cdn.shopify.com/s/files/1/0758/6929/0779/files/Masala_Tea_-_Annams_Recipes_Shop_2_480x480.jpg?v=1732347934", width=200) # height not working
    st.markdown(
        """
        <img src="https://cdn.shopify.com/s/files/1/0758/6929/0779/files/Masala_Tea_-_Annams_Recipes_Shop_2_480x480.jpg?v=1732347934"
             width="200" height="200">
        """,
        unsafe_allow_html=True
    )
    vote1 = st.button("Vote for Masala Chai")

with col2:
    st.header("Adrak Chai")
    # st.image("https://www.jagranimages.com/images/newimg/khanakhazana/06_2023-Adrak_ki_Chai_(1).webp", width=200) # height not working
    st.markdown(
        """
        <img src="https://www.jagranimages.com/images/newimg/khanakhazana/06_2023-Adrak_ki_Chai_(1).webp"
             width="200" height="200">
        """,
        unsafe_allow_html=True
    )
    vote2 = st.button("Vote for Adrak Chai")

if vote1:
    st.success("Thanks for voting for Masala Chai!")
elif vote2:
    st.success("Thanks for voting for Adrak Chai!")


name = st.sidebar.text_input("Enter your name")
tea = st.sidebar.selectbox("Select your favorite tea", ["Masala Chai", "Adrak Chai"])

if name:
    st.sidebar.write(f"Hello, {name}! Your favorite tea is {tea}.")

with st.expander("show Chai Making Process"):
    st.write("""
    1. Boil water
    2. Add Masala
    3. Add tea leaves
    4. Stir
    5. Serve
    """)

st.markdown("### Welcome to chai app")
st.markdown("> Blockquote")