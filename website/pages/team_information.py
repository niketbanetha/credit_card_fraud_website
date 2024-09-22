import streamlit as st
import pandas as pd

st.title("Team Member Details")
df = pd.read_csv(r"C:\Users\user\Documents\College\AI_Project\credit_card_fraud_website\website\data\team_details.csv")
st.table(df)