import streamlit as st
import pandas as pd
import os

dir_path = os.path.dirname(os.path.realpath(__name__))

st.title("Team Member Details")
df = pd.read_csv(dir_path + "/data/team_details.csv")
st.table(df)