import streamlit as st
import pandas as pd
import requests

st.title('NYC and NYS Legislative Bill Tracker')

from src.data_acquisition.api_client import fetch_bills

bills = fetch_bills()  

bills_df = pd.DataFrame(bills)

st.table(bills_df)

selected_bill = st.selectbox("Choose a bill to view details", bills_df['Bill Number'])
bill_details = bills_df[bills_df['Bill Number'] == selected_bill]
st.write(bill_details)



