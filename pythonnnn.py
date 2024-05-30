import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import openpyxl
import numpy as np
import geopandas as gpd
from matplotlib.colors import LinearSegmentedColormap
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import plotly.express as px
import streamlit as st


athlete_events = pd.read_excel(r'Athlete_events.xlsx')




# PLOT 10

world_map = go.Figure(go.Choropleth())

asian_countries = [
    "China", "Japan", "South Korea", "North Korea", "Taiwan", "Hong Kong", "Mongolia", "Macau", "Vietnam", 
    "Laos", "Cambodia", "Thailand", "Myanmar", "Malaysia", "Singapore", "Brunei", "Philippines", "Indonesia", 
    "Timor-Leste", "Afghanistan", "Armenia", "Azerbaijan", "Bahrain", "Bangladesh", "Bhutan", "Cyprus", 
    "Georgia", "India", "Iran", "Iraq", "Israel", "Jordan", "Kazakhstan", "Kuwait", "Kyrgyzstan", 
    "Lebanon", "Maldives", "Nepal", "Oman", "Pakistan", "Palestine", "Qatar", "Saudi Arabia", "Sri Lanka", 
    "Syria", "Tajikistan", "Turkey", "Turkmenistan", "United Arab Emirates", "Uzbekistan", "Yemen"
]

european_countries = [
    "Albania", "Andorra", "Austria", "Belarus", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", 
    "Czech Republic", "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", 
    "Ireland", "Italy", "Latvia", "Lithuania", "Luxembourg", "Malta", "Moldova", "Monaco", "Montenegro", 
    "Netherlands", "North Macedonia", "Norway", "Poland", "Portugal", "Romania", "Russia", "San Marino", 
    "Serbia", "Slovakia", "Slovenia", "Spain", "Sweden", "Switzerland", "Ukraine", "United Kingdom", 
    "Vatican City"
]

african_countries = [
    "Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Cape Verde", 
    "Central African Republic", "Chad", "Comoros", "Congo", "Congo (Democratic Republic of the)", "Djibouti", 
    "Egypt", "Equatorial Guinea", "Eritrea", "Eswatini", "Ethiopia", "Gabon", "Ghana", "Guinea", 
    "Guinea-Bissau", "Ivory Coast", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", 
    "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Rwanda", "Sao Tome and Principe", 
    "Senegal", "Seychelles", "Sierra Leone", "Somalia", "South Africa", "South Sudan", "Sudan", "Tanzania", 
    "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"
]

american_countries = [
    "Suriname", "Trinidad and Tobago", "Argentina", "Bahamas", "Barbados", "Belize", "Bolivia", "Brazil", 
    "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominica", "Dominican Republic", "Ecuador", "El Salvador", 
    "Grenada", "Guatemala", "Guyana", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", 
    "Peru", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "United States", "Uruguay", 
    "Venezuela"
]


all_countries = asian_countries + european_countries + african_countries + american_countries

athlete_counts = athlete_events[
    (athlete_events['Team'].isin(all_countries)) & (athlete_events['Year'].between(1990, 2016))
].groupby('Team')['ID'].nunique().reset_index(name='athlete_count')

world_map = go.Figure(go.Choropleth(
    locations=athlete_counts['Team'],
    z=athlete_counts['athlete_count'],
    locationmode='country names',
    colorscale='Blues',
    marker_line_color='white',
    colorbar_title='Athlete Count',
))

world_map.update_layout(
    title='Number of Athletes in Asian, European, African, and American Countries (1990-2016)',
    geo=dict(
        showcoastlines=True,
        showcountries=True,
        countrycolor='white',
        coastlinecolor='black'
    ),
    hoverlabel=dict(
        bgcolor="white",
        font_size=16,
        font_family="Arial"
    )
)

st.plotly_chart(world_map)
