import streamlit as st
import pandas as pd

# Read the Excel file
file_path = r"C:\Users\admin\OneDrive\文档\GitHub\Python\Athlete_events.xlsx"
try:
    athlete_events = pd.read_excel(file_path)
except FileNotFoundError as e:
    st.error(f"File not found error: {e}")
except Exception as e:
    st.error(f"An error occurred: {e}")

# Display the data
st.write(athlete_events)
