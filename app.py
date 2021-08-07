import streamlit as st
from follow_page import show_follow_page

menu=["Follow"]
page = st.sidebar.selectbox("Menu", menu)

if page == "Follow":
    show_follow_page()

else:
    pass