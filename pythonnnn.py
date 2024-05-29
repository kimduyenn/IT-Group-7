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


b_data = athlete_events[athlete_events['Sport'].isin(["Boxing", "Football", "Judo", "Swimming", "Taekwondo"])]

athlete_counts = b_data['Sport'].value_counts().reset_index()
athlete_counts.columns = ['Sport', 'Count']

color_sequence = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]

fig = px.pie(
    athlete_counts,
    values='Count',
    names='Sport',
    title='The number of athletes participating in the Olympic during 120 Years',
    hole=0.7,  # To create a donut chart
    color_discrete_sequence=color_sequence
)

st.plotly_chart(fig)

# PLOT 5

filtered_dat = athlete_events[(athlete_events['Season'] == "Summer") & (athlete_events['Year'] >= 1990) & (athlete_events['Year'] <= 2016)]
filtered_dat = filtered_dat[['Weight', 'Sex']].dropna()
filtered_dat['Weight'] = pd.to_numeric(filtered_dat['Weight'])

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

fig.update_layout(
    title_text='Distribution of Athletes’ Weights by Gender (Summer Olympics 1990-2016)',
    xaxis_title_text='Weight (kg)',
    yaxis_title_text='Number of Athletes',
    barmode='overlay',
    bargap=0.1,
    bargroupgap=0.1,
    legend_title_text='Gender'
)

st.plotly_chart(fig)


# PLOT 6


athlete_events = pd.DataFrame({
    'Year': np.random.randint(1990, 2023, 1000),
    'Season': np.random.choice(['Summer', 'Winter'], 1000),
    'Sport': np.random.choice(['Athletics', 'Swimming', 'Skiing', 'Cycling', 'Gymnastics'], 1000)
})

st.title('Olympic Sports Participation')
st.write('Number of Sports Participated in Summer and Winter Seasons (1990-2022)')

filtered_dat = athlete_events[athlete_events['Year'] >= 1990]
filtered_dat = filtered_dat[['Year', 'Season', 'Sport']].drop_duplicates()

sports_count = filtered_dat.groupby(['Year', 'Season']).size().unstack(fill_value=0)

years = sports_count.index
summer_counts = sports_count['Summer']
winter_counts = sports_count['Winter']

fig, axs = plt.subplots(2, 1, figsize=(12, 12))

axs[0].bar(years, summer_counts, color='#FFA500', alpha=0.7, label='Summer')
axs[0].set_xlabel('Year')
axs[0].set_ylabel('Number of Sports')
axs[0].set_title('Number of Sports Participated in Summer Season (1990-2022)')
axs[0].legend()
axs[0].grid(True, linestyle='-', alpha=0.2)

for i, summer_count in enumerate(summer_counts):
    axs[0].text(years[i], summer_count, str(summer_count), ha='center', va='bottom', fontsize=10)

axs[1].bar(years, winter_counts, color='#4682B4', alpha=0.7, label='Winter')
axs[1].set_xlabel('Year')
axs[1].set_ylabel('Number of Sports')
axs[1].set_title('Number of Sports Participated in Winter Season (1990-2022)')
axs[1].legend()
axs[1].grid(True, linestyle='-', alpha=0.2)

for i, winter_count in enumerate(winter_counts):
    axs[1].text(years[i], winter_count, str(winter_count), ha='center', va='bottom', fontsize=10)

st.pyplot(fig)



# PLOT 7


year2002 = athlete_events[athlete_events['Year'] == 2002]

year2002['Age'] = pd.to_numeric(year2002['Age'], errors='coerce')

year2002_count = year2002.drop_duplicates(subset=['ID', 'Age', 'Sex'])

year2002_count = year2002_count.groupby(['Age', 'Sex']).size().reset_index(name='count')

fig = go.Figure()

for sex, color in zip(['M', 'F'], ['blue', 'red']):
    data = year2002_count[year2002_count['Sex'] == sex]
    fig.add_trace(go.Scatter(
        x=data['Age'],
        y=data['count'],
        mode='lines',
        fill='tozeroy',
        name=sex,
        line=dict(color=color),
        hovertemplate='<b>%{x}</b><br><br>Athletes: %{y}',
    ))

fig.update_layout(
    title='Density Chart with Athlete Count by Age and Sex in 2002',
    xaxis_title='Age',
    yaxis_title='Athletes',
    legend_title='Sex',
    legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="right",
        x=0.99
    ),
    showlegend=True,
    hovermode='x'
)

st.plotly_chart(fig)


# PLOT 8


filtered_dat = athlete_events[(athlete_events['Year'] >= 1990) & (athlete_events['Year'] <= 2016)]

summary_dat = filtered_dat.groupby(['Year', 'Season']).size().reset_index(name='total_athletes')

fig = go.Figure()

for season, color in zip(['Summer', 'Winter'], ['darkorange', 'steelblue']):
    data = summary_dat[summary_dat['Season'] == season]
    fig.add_trace(go.Scatter(
        x=data['Year'],
        y=data['total_athletes'],
        mode='lines+markers',
        name=season,
        line=dict(color=color),
        marker=dict(color=color, size=8),
        text=data['total_athletes'],
        hovertemplate='<b>%{x}</b><br><br>Total Athletes: %{y}',
    ))

fig.update_layout(
    title='Total Athletes in Summer and Winter (1990-2016)',
    xaxis_title='Year',
    yaxis_title='Total Athletes',
    legend_title='Season',
    legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="right",
        x=0.99
    ),
    showlegend=True,
    hovermode='x'
)

st.plotly_chart(fig)


# plot 9


selected_sports = ["Basketball", "Gymnastics", "Swimming", "Athletics", "Boxing", "Wrestling"]

sport_age = athlete_events[(athlete_events['Year'] >= 1960) & (athlete_events['Year'] <= 2000) & athlete_events['Sport'].isin(selected_sports)]

sport_age['Year'] = pd.to_numeric(sport_age['Year'], errors='coerce')
sport_age['Age'] = pd.to_numeric(sport_age['Age'], errors='coerce')

sport_medians = sport_age.groupby('Sport')['Age'].median().sort_values().index

sport_colors = {
    "Basketball": "#1f77b4",  
    "Gymnastics": "#ff7f0e",  
    "Swimming": "#2ca02c",     
    "Athletics": "#d62728",    
    "Boxing": "#9467bd",       
    "Wrestling": "#8c564b"     
}

fig = go.Figure()

for sport in sport_medians:
    data = sport_age[sport_age['Sport'] == sport]
    fig.add_trace(go.Box(
        x=data['Sport'],
        y=data['Age'],
        name=sport,
        marker_color=sport_colors[sport],  
        boxmean='sd',
        hoverinfo='y+name',
        boxpoints='all'
    ))

fig.update_layout(
    title='Distribution of Age by Sport (1960-2000)',
    xaxis_title='Sport',
    yaxis_title='Age',
    showlegend=True,
    hovermode='closest'
)
st.plotly_chart(fig)



# PLOT 10



world_map = go.Figure(go.Choropleth())

east_asian_countries = [
    "China", "Japan", "South Korea", "North Korea", "Taiwan", "Hong Kong", "Mongolia", "Macau", "Vietnam", 
    "Laos", "Cambodia", "Thailand", "Myanmar", "Malaysia", "Singapore", "Brunei", "Philippines", "Indonesia", 
    "Timor-Leste"]

athlete_counts = athlete_events[
    (athlete_events['Team'].isin(east_asian_countries)) & (athlete_events['Year'].between(1990, 2016))
].groupby('Team')['ID'].nunique().reset_index(name='athlete_count')

world_map.add_trace(go.Choropleth(
    locations=athlete_counts['Team'],
    z=athlete_counts['athlete_count'],
    text=athlete_counts['Team'],
    colorscale='Blues',
    marker_line_color='white',
    colorbar_title='Athlete Count',
))

world_map.update_layout(
    title='Number of Athletes in East Asian Countries (1990-2016)',
    geo=dict(
        showcoastlines=True,
        showcountries=True,
        countrycolor='white',
        coastlinecolor='black'
    )
)

st.plotly_chart(world_map)
