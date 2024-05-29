import pandas as pd
import matplotlib.pyplot as plt
import openpyxl
import numpy as np
import geopandas as gpd
from matplotlib.colors import LinearSegmentedColormap
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import plotly.express as px
import streamlit as st
athlete_events = pd.read_excel(r'Athlete_events.xlsx')


# PLOT 1


# Filter data for the selected sports in 2016
selected_sports = ["Athletics", "Badminton", "Boxing", "Cycling", "Gymnastics", "Swimming"]
my_data = athlete_events[(athlete_events['Year'] == 2016) & (athlete_events['Sport'].isin(selected_sports))]

# Calculate the percentage of athletes in each sport
sport_counts = my_data['Sport'].value_counts(normalize=True) * 100

# Create the pie chart with Plotly Express
fig = px.pie(values=sport_counts, names=sport_counts.index, title='Distribution of Athletes in Selected Sports (2016)', hole=0.1)
fig.update_traces(textposition='inside', textinfo='percent+label')

# Display the chart in Streamlit
st.plotly_chart(fig)


