import streamlit as st
from src.config import Config
from src.database import Database
from src.session_state import get_session_state

session_state = get_session_state()

st.title('Legislative Bill Tracker')
st.sidebar.header('Search for Bills')

bill_number = st.sidebar.text_input('Bill Number')
search_results = session_state.search_bills(bill_number)

if search_results:
    for bill in search_results:
        st.write(bill)

