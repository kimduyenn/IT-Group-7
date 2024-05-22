import streamlit as st
import pandas as pd




# Title
st.title('My First Streamlit App')

# Load Excel file
try:
    athlete_events = pd.read_excel('Athlete_events.xlsx')
    st.write(athlete_events.head())
except FileNotFoundError:
    st.error("File not found. Please make sure the file 'Athlete_events.xlsx' exists in the same directory as this script.")
