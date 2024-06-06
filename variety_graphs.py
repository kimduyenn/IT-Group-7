import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
color_theme_list = ['blues', 'cividis', 'greens', 'inferno', 'magma', 'plasma', 'reds', 'rainbow', 'turbo', 'viridis']
selected_color_theme = st.selectbox('Select a color theme', color_theme_list)

# Load the data
file_path = 'Athlete_events.xlsx'
df = pd.read_excel(file_path)

# Title of the app
st.title('Olympic Athletes Analysis')

# Sidebar for user input
st.sidebar.title("Filter Options")

# Convert NOC to country names using an example mapping (you should replace this with a complete mapping)
noc_to_country = {
    'USA': 'United States',
    'GBR': 'United Kingdom',
    'CHN': 'China',
    'RUS': 'Russia',
    'GER': 'Germany',
    'AUS': 'Australia',
    # Add all other NOCs with their respective country names
}

# Add a full mapping for all NOCs from a reliable source or manually add the NOCs
df['Country'] = df['NOC'].map(noc_to_country)

# List of unique countries for selection, remove NaN values if any
country_list = df['Country'].dropna().unique()
country_list.sort()

# Sidebar for country selection
country = st.sidebar.selectbox('Select a Country', country_list)

# Filter data based on the selected country
filtered_data = df[df['Country'] == country]

# Introduction
st.markdown("""
## Introduction
This dashboard provides a comprehensive analysis of Olympic athletes' data. Use the sidebar to filter by country and sport, and explore various visualizations including age distribution, medal distribution, country participation, and more.
""")

# Sidebar for sport selection
sport_list = filtered_data['Sport'].unique()
sport = st.sidebar.selectbox('Select a Sport', sport_list)

# Filter data further based on the selected sport
filtered_data = filtered_data[filtered_data['Sport'] == sport]

# Plotting - Histogram for Age Distribution
st.header("Age Distribution of Athletes")
fig, ax = plt.subplots()
sns.histplot(filtered_data['Age'].dropna(), kde=True, ax=ax)
ax.set_title(f'Age Distribution of Athletes in {sport} from {country}')
ax.set_xlabel('Age')
ax.set_ylabel('Frequency')
st.pyplot(fig)

# Plotting - Pie Chart for Medal Distribution
st.header("Medal Distribution")
medal_counts = filtered_data['Medal'].value_counts()
fig_pie = px.pie(values=medal_counts.values, names=medal_counts.index, title=f'Medal Distribution in {sport} from {country}')
st.plotly_chart(fig_pie)

# Plotting - Bar Chart for Sport Participation within the Country
st.header("Top 10 Sports by Number of Athletes")
sport_counts = df[df['Country'] == country]['Sport'].value_counts().head(10)
fig_bar = px.bar(x=sport_counts.index, y=sport_counts.values, labels={'x':'Sport', 'y':'Number of Athletes'}, title=f'Top 10 Sports by Number of Athletes in {country}')
st.plotly_chart(fig_bar)

# Plotting - Line Graph for Number of Athletes over the Years
st.header("Number of Athletes Over the Years")
year_counts = filtered_data['Year'].value_counts().sort_index()
fig_line = px.line(x=year_counts.index, y=year_counts.values, labels={'x':'Year', 'y':'Number of Athletes'}, title=f'Number of Athletes Over the Years in {sport} from {country}')
st.plotly_chart(fig_line)

# Plotting - Donut Chart for Gender Distribution
st.header("Gender Distribution")
gender_counts = filtered_data['Sex'].value_counts()
fig_donut = go.Figure(data=[go.Pie(labels=gender_counts.index, values=gender_counts.values, hole=.3)])
fig_donut.update_layout(title_text=f'Gender Distribution in {sport} from {country}')
st.plotly_chart(fig_donut)

# Plotting - Tree Map for Events in the Selected Sport
st.header("Events in the Selected Sport")
event_counts = filtered_data['Event'].value_counts().reset_index()
event_counts.columns = ['Event', 'Count']
fig_tree = px.treemap(event_counts, path=['Event'], values='Count', title=f'Events in {sport} from {country}')
st.plotly_chart(fig_tree)

# Plotting - Heatmap for Number of Athletes by Country and Year
st.header("Number of Athletes by Country and Year")
heatmap_data = filtered_data.groupby(['Country', 'Year']).size().unstack(fill_value=0)
fig_heatmap = px.imshow(heatmap_data, labels=dict(x="Year", y="Country", color="Number of Athletes"),
                        title=f'Number of Athletes by Country and Year in {sport}', 
                        x=heatmap_data.columns, y=heatmap_data.index)
st.plotly_chart(fig_heatmap)

