import streamlit as st
import os

dir_path = os.path.dirname(os.path.realpath(__name__))
st.header("Project Plan Flow Chart")
st.image(dir_path + "/data/Project Plan.jpg")