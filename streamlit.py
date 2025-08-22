import streamlit as st

# Title & description
st.title("🚀 My First Streamlit App")
st.write("This is a simple demo without any machine learning model.")

# User input
name = st.text_input("Enter your name:")
age = st.slider("Select your age:", 1, 100, 25)

# Button & output
if st.button("Submit"):
    st.success(f"Hello {name}, you are {age} years old! 🎉")
