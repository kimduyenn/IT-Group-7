import streamlit as st
import pandas as pd


# Specify the file path
file_path = r"C:\Users\admin\OneDrive\文档\GitHub\Python\Athlete_events.xlsx"

# Read the Excel file
try:
    athlete_events = pd.read_excel(file_path)
    print(athlete_events.head())
except FileNotFoundError as e:
    print(f"File not found error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")

# Title
st.title('My First Streamlit App')

# Load Excel file
try:
    athlete_events = pd.read_excel('Athlete_events.xlsx')
    st.write(athlete_events.head())
except FileNotFoundError:
    st.error("File not found. Please make sure the file 'Athlete_events.xlsx' exists in the same directory as this script.")
