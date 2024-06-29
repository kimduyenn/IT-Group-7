import streamlit as st 
import pandas as pd 
import numpy as np
import json
import streamlit_lottie as st_lottie
import requests
from streamlit_extras.colored_header import colored_header
from annotated_text import annotated_text
from PIL import Image
from streamlit_extras.stoggle import stoggle
from streamlit_extras.let_it_rain import rain
import matplotlib.pyplot as plt
import plotly.express as px

# Page configuration
st.set_page_config(page_title="PYTHON 2 - BUSINESS IT 2", page_icon="🥰", layout="wide")

# Header and description
st.subheader("Group 7")
st.title("PYTHON 2 - BUSINESS IT 2 :blue_heart:")
st.write("We are a group of business students who are interested in the economical situation in the world. Therefore, we decided to analyze a set of data about the employment fluctuation in the USA from 1978 to 2022. Through this visualization, we hope to bring a clear vision to people about how the labor market in the USA has changed over the past decades.")

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
st.write("[Accessing our dataset >](https://python-itpython2group7.streamlit.app/)") 

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
    description="Get to know about our group",
    color_name="light-blue-70",
)

# Group members information
st.subheader("**Full name: Tran Thi Thuy Trang**")
st.write("Student ID: 10323060")
st.write("Email: 10323060@student.vgu.edu.vn")
st.write("Major: Finance & Accounting (BFA)")

st.subheader("**Full name: Tran Ngoc My Thao**")
st.write("Student ID: 10323059")
st.write("Email: 10323059@student.vgu.edu.vn")
st.write("Major: Finance & Accounting (BFA)")

st.subheader("**Full name: Luong Nu Mai Nhung**")
st.write("Student ID: 10323056")
st.write("Email: 10323056@student.vgu.edu.vn")
st.write("Major: Finance & Accounting (BFA)")

st.subheader("**Full name: Kim Duyen**")
st.write("Student ID: 10323044")
st.write("Email: 10323044@student.vgu.edu.vn")
st.write("Major: Finance & Accounting (BFA)")

st.markdown("---")
