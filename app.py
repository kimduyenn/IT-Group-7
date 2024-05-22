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
import streamlit as st
import pandas as pd

# Define the URL of the Excel file on GitHub
file_url = "https://github.com/kimduyenn/Python/raw/main/Athlete_events.xlsx"

# Read the Excel file
try:
    athlete_events = pd.read_excel(file_url)
except Exception as e:
    st.error(f"An error occurred while reading the Excel file: {e}")

# Display the data
st.write(athlete_events)
