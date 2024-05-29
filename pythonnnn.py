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


# PLOT 1

selected_sports = ["Athletics", "Badminton", "Boxing", "Cycling", "Gymnastics", "Swimming"]
my_data = athlete_events[(athlete_events['Year'] == 2016) & (athlete_events['Sport'].isin(selected_sports))]

sport_counts = my_data['Sport'].value_counts(normalize=True) * 100

fig = px.pie(values=sport_counts, names=sport_counts.index, title='Distribution of Athletes in Selected Sports (2016)', hole=0.1)
fig.update_traces(textposition='inside', textinfo='percent+label')

st.plotly_chart(fig)


# PLOT 2

Year2014 = athlete_events[athlete_events['Year'] == 2014]
Teams = ["United States", "Russia", "Norway", "Germany", "Canada"]
m_data = Year2014[Year2014['Team'].isin(Teams)]

m_data_unique = m_data.drop_duplicates(subset='Name', keep='first')

team_counts = m_data_unique['Team'].value_counts().reset_index()
team_counts.columns = ['Team', 'Count']
team_counts = team_counts.sort_values(by='Count', ascending=False)

unique_colors = ["#FF5733", "#FFBD33", "#33FF57", "#33FFBD", "#5733FF"]

fig = px.bar(
    team_counts,
    x='Count',
    y='Team',
    orientation='h',
    color='Team',
    color_discrete_sequence=unique_colors,
    title="The number of athletes participating from five countries in the 2014 Winter Olympics",
    labels={'Count': 'Athletes', 'Team': 'Countries'}
)

fig.update_layout(
    yaxis=dict(categoryorder='total ascending'),
    showlegend=False
)

st.plotly_chart(fig)



# PLOT 3

filtered_data = athlete_events[(athlete_events['Year'] >= 1990) & (athlete_events['Year'] <= 2016)]
filtered_data = filtered_data.dropna(subset=['Sex'])

yearly_gender_counts = filtered_data.groupby(['Year', 'Sex']).size().unstack(fill_value=0)

yearly_gender_counts['Total'] = yearly_gender_counts['M'] + yearly_gender_counts['F']
yearly_gender_counts.sort_values(by='Year', inplace=True)

fig = go.Figure()

fig.add_trace(go.Bar(
    x=yearly_gender_counts.index,
    y=yearly_gender_counts['M'],
    name='Male',
    marker_color='#FF6666',
    text=yearly_gender_counts['M'],
    textposition='auto'
))

fig.add_trace(go.Bar(
    x=yearly_gender_counts.index,
    y=yearly_gender_counts['F'],
    name='Female',
    marker_color='#FF9966',
    text=yearly_gender_counts['F'],
    textposition='auto'
))
fig.update_layout(
    title='Number of Athletes by Gender (1990-2016)',
    xaxis_title='Year',
    yaxis_title='Number of Athletes',
    barmode='stack',
    legend_title_text='Sex',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis=dict(tickmode='linear'),
    yaxis=dict(gridcolor='rgba(128,128,128,0.1)'),
    showlegend=True
)

st.plotly_chart(fig)


# PLOT 4
filtered_dat = athlete_events[(athlete_events['Season'] == "Summer") & (athlete_events['Year'] >= 1990) & (athlete_events['Year'] <= 2016)]
filtered_dat = filtered_dat[['Weight', 'Sex']].dropna()
filtered_dat['Weight'] = pd.to_numeric(filtered_dat['Weight'])

# Create histograms using Plotly
fig = go.Figure()

fig.add_trace(go.Histogram(
    x=filtered_dat[filtered_dat['Sex'] == 'M']['Weight'],
    name='Male',
    xbins=dict(start=0, end=300, size=5),
    marker_color='#1f77b4',
    opacity=0.75
))

fig.add_trace(go.Histogram(
    x=filtered_dat[filtered_dat['Sex'] == 'F']['Weight'],
    name='Female',
    xbins=dict(start=0, end=300, size=5),
    marker_color='#E54646',
    opacity=0.75
))

# Update layout
fig.update_layout(
    title_text='Distribution of Athletes’ Weights by Gender (Summer Olympics 1990-2016)',
    xaxis_title_text='Weight (kg)',
    yaxis_title_text='Number of Athletes',
    barmode='overlay',
    bargap=0.1,
    bargroupgap=0.1
)

# Display the chart in Streamlit
st.plotly_chart(fig)
