import streamlit as st
import pandas as pd
st.title("File Upload Example")
file=st.file_uploader("Upload a Pdf file",type=["pdf"])
if file:
    st.success("File uploaded successfully")
elif file is None:
    st.warning("Please upload a file")

st.title("CSV File Upload Example")
fil=st.file_uploader("Upload a CSV file",type=["csv"])
if fil:
    df=pd.read_csv(fil)
    st.dataframe(df)
elif fil is None:
    st.warning("Please upload a file")
st.title("Image File Upload Example")
file2=st.file_uploader("Upload an Image file",type=["jpg","png"])
if file2:
    st.image(file2,caption="Uploaded Image",use_column_width=True)
elif file2 is None:
    st.error("Please upload an image file")
