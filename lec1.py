import streamlit as st
st.title("Programming Languages")
st.subheader("This is the subheader")
lang=st.selectbox("Choose a programming language:", ["Python", "JavaScript", "Java", "C++"])
st.write("You choose this programming language",lang)
st.success("The task is successfully completed")