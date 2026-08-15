import streamlit as st
st.title("Movie Recommendation App")
st.sidebar.title("Movie Recommendation Card")
st.sidebar.selectbox("Choose a movie genre:", ["Action", "Comedy", "Drama", "Horror", "Romance"])
st.sidebar.selectbox("Select the Language:", ["English", "Spanish", "French", "German", "Japanese"])
st.sidebar.slider("Select Rating:", 0, 10, 5)
st.markdown("### Recommended Movies")
col1, col2, col3 = st.columns(3)
with col1:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTQMUS4m5gi_nNHSQH47yGtK2JHXtTOuVvrXlDTAbLPXA&s=10",width=200)
    st.write("BodyGuard")
    st.button("Watch Now BodyGuard")
with col2:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS5bI-rBvMcD7rQwx4pPsVm7UlJzOCRLCB6LPmHB7paJg&s=10",width=200)
    st.write("Sikandar")
    st.button("Watch Now Sikandar")

with col3:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQZQRe8toDDoZ2SwJHhUlqwTCgV3sK5RBVKGwZbI-l0-A&s=10",width=200)
    st.write("Kick")
    st.button("Watch Now Kick")


