import streamlit as st 
import pandas as pd 
import numpy as np
import json
import requests
import streamlit_lottie as st_lottie
import plotly.express as px
import matplotlib.pyplot as plt
from PIL import Image
from streamlit_extras.colored_header import colored_header
from streamlit_extras.stoggle import stoggle
from streamlit_extras.let_it_rain import rain
from annotated_text import annotated_text

# Page configuration
st.set_page_config(page_title="PYTHON 2 - BUSINESS IT 2", page_icon="🥰", layout="wide")

# Header and description
st.subheader("Group 7")
st.title("PYTHON 2 - BUSINESS IT 2 :blue_heart:")
st.write("We are a group of business students who are interested in the economic situation in the world. Therefore, we decided to analyze a dataset about the employment fluctuation in the USA from 1978 to 2022. Through this visualization, we hope to provide a clear view of how the US labor market has evolved over the decades.")

# Group information toggle
stoggle(
    "Group information",
    """
    1. Tran Thi Thuy Trang - 10323060
    2. Tran Ngoc My Thao - 10323059
    3. Luong Nu Mai Nhung - 10323056
    4. Kim Duyen - 10323044
    """
)
st.write("[Accessing our dataset >](https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results)") 

# Adding rain effect
rain(
    emoji="💕",
    font_size=54,
    falling_speed=5,
    animation_length="3",
)

# Group members introduction header
colored_header(
    label="Group members introduction",
    description="Get to know our group",
    color_name="light-blue-70",
)

# Group members information
members_info = [
    {"name": "Tran Thi Thuy Trang", "student_id": "10323060", "email": "10323060@student.vgu.edu.vn", "major": "Finance & Accounting (BFA)"},
    {"name": "Tran Ngoc My Thao", "student_id": "10323059", "email": "10323059@student.vgu.edu.vn", "major": "Finance & Accounting (BFA)"},
    {"name": "Luong Nu Mai Nhung", "student_id": "10323056", "email": "10323056@student.vgu.edu.vn", "major": "Finance & Accounting (BFA)"},
    {"name": "Kim Duyen", "student_id": "10323044", "email": "10323044@student.vgu.edu.vn", "major": "Finance & Accounting (BFA)"}
]

for member in members_info:
    st.subheader(f"**Full name: {member['name']}**")
    st.write(f"Student ID: {member['student_id']}")
    st.write(f"Email: {member['email']}")
    st.write(f"Major: {member['major']}")

st.markdown("---")
