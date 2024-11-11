import streamlit as st
import pandas as pd 

DEBIT = ["debit", "Debit", "DEBIT", "Db"]
CREDIT = ["credit", "Credit", "CREDIT", "Cr"]

# provide user to select column which provide information about
# transaction type and amount debited or credited
def create_column_selection_button(dataframe):
    column_names = dataframe.columns
    
    transaction_type_selection = st.selectbox(label="Select column which inform about transaction type",
                                              options= column_names)
    amount_column_seclection = st.selectbox(label = "Select column which provide information about transaction amount",
                                            options=column_names)
    st.divider()
    return transaction_type_selection, amount_column_seclection

def calculate_total_expenditure(dataframe, trans_type_col, amount_col):
    try:

        total_credit_amount = dataframe[dataframe[trans_type_col].isin(CREDIT)][amount_col].sum()
        highest_credit_amount = dataframe[dataframe[trans_type_col].isin(CREDIT)][amount_col].max()
        smallest_credit_amount = dataframe[dataframe[trans_type_col].isin(CREDIT)][amount_col].min()
        avg_credit_amount = (highest_credit_amount+smallest_credit_amount)/2

        total_debit_amount = dataframe[dataframe[trans_type_col].isin(DEBIT)][amount_col].sum()
        highest_debit_amount = dataframe[dataframe[trans_type_col].isin(DEBIT)][amount_col].max()
        smallest_debit_amount = dataframe[dataframe[trans_type_col].isin(DEBIT)][amount_col].min()
        avg_debit_amount = (highest_debit_amount + smallest_debit_amount)/2

        st.subheader("Expenditure Analysis")
        st.text("Total Debited Amount: " + str(total_debit_amount))
        st.text("Highest Debited Amount: "+ str(highest_debit_amount))
        st.text("Smallest Debited Amount: " + str(smallest_debit_amount))
        st.text("Average Debited Amount: "+str(avg_debit_amount))
        st.text("Debit transactions which could be suspicious")
        st.dataframe(dataframe[dataframe[trans_type_col].isin(DEBIT)][dataframe[amount_col]>=avg_debit_amount])

        st.text("Total Credited Amount: " + str(total_credit_amount))
        st.text("Highest Credited Amount: "+ str(highest_credit_amount))
        st.text("Smallest Credited Amount: " + str(smallest_credit_amount))
        st.text("Average Credited Amount: "+str(avg_credit_amount))
        st.text("Credit transactions which could be suspicious")
        st.dataframe(dataframe[dataframe[trans_type_col].isin(CREDIT)][dataframe[amount_col]>=avg_debit_amount])
        
        
    except:
        st.subheader("Expenditure Analysis")
        st.error("Incorrect column selected.")
        st.divider()


if __name__=="__main__":

    st.header("Project: Credit Card Fraud Detection")
    st.header("Group Number: 22")

    file_uploaded = st.file_uploader("Upload Bank Statement Excel or CSV File", accept_multiple_files=False, type=["csv", "xls"])

    if file_uploaded is not None:
        st.divider()
        dataframe = pd.read_csv(file_uploaded)
        st.text("First 5 rows of the uploaded statement")
        st.dataframe(dataframe.head())
        st.divider()
        trans_type_column, amount_column = create_column_selection_button(dataframe)
        
        if trans_type_column != amount_column:
            calculate_total_expenditure(dataframe, trans_type_column, amount_column)