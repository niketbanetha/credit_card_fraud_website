import streamlit as st

st.header("Project sub-domain research")
st.markdown('''
Credit card fraud has become a pervasive issue in today's digital age, fueled by the 
growth of online transactions and e-commerce. Fraudsters exploit stolen card information 
for unauthorized purchases or fraudulent activities. To combat this problem, credit card 
fraud detection systems have been developed. This project aims to address key 
challenges, including:\n
• **Class imbalance**: The scarcity of fraudulent transactions compared to legitimate 
ones can bias models. We investigate under sampling techniques to mitigate this.\n
• **Data stream dynamics**: Fraud patterns evolve, and spending behaviors change. 
We explore methods to handle unbalanced and non-stationary data streams.\n
• **Performance evaluation**: We aim to assess performance using metrics relevant 
to fraud detection, considering the costs of false positives and negatives.\n
• **Feedback integration**: We propose incorporating investigator feedback to refine 
models and improve alert accuracy.\n
Ultimately, our goal is to design a robust fraud detection system that can effectively 
identify fraudulent transactions, protect consumers, and mitigate financial losses.
            ''')
