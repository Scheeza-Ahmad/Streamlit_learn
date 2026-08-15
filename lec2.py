import streamlit as st
from datetime import date

st.title("Age Calculator")
name = st.text_input("Enter your name")
dob = st.date_input(
    "Enter your date of birth",
    min_value=date(1900, 1, 1),
    max_value=date.today(),
    value=date(2000, 1, 1)  # default starting point
)

if st.button("Calculate Age"):
    today = date.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    st.write(f"Hello {name}, you are {age} years old.")