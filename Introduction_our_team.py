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
st.title("PYTHON 2 - BUSINESS IT 2 :orange_heart:")
st.write("We are a group of business students who are interested in the economical situation in the world. Therefore, we decided to analyze a set of data about the employment fluctuation in the USA from 1978 to 2022. Through this visualization, we hope to bring a clear vision to people about how the labor market in the USA has changed over the past decades.")

# Group information toggle
stoggle(
    "Group information",
    """
    1. Dinh Ha Tu Van - 10622045
    2. Bui Cam Ha Quyen - 10622023
    3. Mai Hong Hanh - 10622014
    """
)

st.write("[Accessing our dataset >](https://docs.google.com/spreadsheets/d/1HbBDpeXYXhl3MQU2bZ-YZiHb1Fe2COrT/edit?usp=drive_link&ouid=114022649098492793407&rtpof=true&sd=true)")

# Adding rain effect
rain(
    emoji="❤️",
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

# Group member 1
tv2 = st.columns(2)

with tv2:
    st.subheader("**Full name: Dinh Ha Tu Van (Group leader)**")
    st.write("Student ID: 10622045")
    st.write("Email: 10622045@student.vgu.edu.vn")
    st.write("Major: Business Administration (BBA)")
    st.write("Phone number: 077 6209215")

st.write(" ")

# Group member 2
hq2 = st.columns(2)

with hq2:
    st.subheader("**Full name: Bui Cam Ha Quyen**")
    st.write("Student ID: 10622023")
    st.write("Email: 10622023@student.vgu.edu.vn")
    st.write("Major: Finance & Accounting (BFA)")
    st.write("Phone number: 090 8784370")

st.write(" ")

# Group member 3
mh2 = st.columns(2)

with mh2:
    st.subheader("**Full name: Mai Hong Hanh**")
    st.write("Student ID: 10622014")
    st.write("Email: 10622014@student.vgu.edu.vn")
    st.write("Major: Business Administration (BBA)")
    st.write("Phone number: 039 2230636")

st.markdown("---")

# Contact form
st.subheader("💬 Leave us your message!")
st.caption("Let us know if you have any recommendations")

contactform = """
<form action="https://formsubmit.co/10622045@student.vgu.edu.vn" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your name" required>
    <input type="email" name="email" placeholder="Your email address" required>
    <textarea name="message" placeholder="What do you think?"></textarea>
    <button type="submit">Send</button>
</form>
"""
st.markdown(contactform, unsafe_allow_html=True)

# Local CSS function
def local_css(style):
    with open(style) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style.css")
