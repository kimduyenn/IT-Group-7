import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

# Load the data
file_path = 'Athlete_events.xlsx'
df = pd.read_excel(file_path)

# Title of the app
st.title('Olympic Athletes Analysis')

# Sidebar for user input
st.sidebar.title("Filter Options")
sport = st.sidebar.selectbox('Select a Sport', df['Sport'].unique())

# Filter data based on the selected sport
filtered_data = df[df['Sport'] == sport]

# Introduction
st.markdown("""
## Introduction
This dashboard provides a comprehensive analysis of Olympic athletes' data. Use the sidebar to filter by sport and explore various visualizations including age distribution, medal distribution, country participation, and more.
""")

# Plotting - Histogram for Age Distribution
st.header("Age Distribution of Athletes")
fig, ax = plt.subplots()
sns.histplot(filtered_data['Age'].dropna(), kde=True, ax=ax)
ax.set_title(f'Age Distribution of Athletes in {sport}')
ax.set_xlabel('Age')
ax.set_ylabel('Frequency')
st.pyplot(fig)

# Plotting - Pie Chart for Medal Distribution
st.header("Medal Distribution")
medal_counts = filtered_data['Medal'].value_counts()
fig_pie = px.pie(values=medal_counts.values, names=medal_counts.index, title=f'Medal Distribution in {sport}')
st.plotly_chart(fig_pie)

# Plotting - Bar Chart for Country Participation
st.header("Top 10 Countries by Number of Athletes")
country_counts = filtered_data['NOC'].value_counts().head(10)
fig_bar = px.bar(x=country_counts.index, y=country_counts.values, labels={'x':'Country', 'y':'Number of Athletes'}, title=f'Top 10 Countries by Number of Athletes in {sport}')
st.plotly_chart(fig_bar)

# Plotting - Line Graph for Number of Athletes over the Years
st.header("Number of Athletes Over the Years")
year_counts = filtered_data['Year'].value_counts().sort_index()
fig_line = px.line(x=year_counts.index, y=year_counts.values, labels={'x':'Year', 'y':'Number of Athletes'}, title=f'Number of Athletes Over the Years in {sport}')
st.plotly_chart(fig_line)

# Plotting - Donut Chart for Gender Distribution
st.header("Gender Distribution")
gender_counts = filtered_data['Sex'].value_counts()
fig_donut = go.Figure(data=[go.Pie(labels=gender_counts.index, values=gender_counts.values, hole=.3)])
fig_donut.update_layout(title_text=f'Gender Distribution in {sport}')
st.plotly_chart(fig_donut)

# Plotting - Tree Map for Events in the Selected Sport
st.header("Events in the Selected Sport")
event_counts = filtered_data['Event'].value_counts().reset_index()
event_counts.columns = ['Event', 'Count']
fig_tree = px.treemap(event_counts, path=['Event'], values='Count', title=f'Events in {sport}')
st.plotly_chart(fig_tree)

# Plotting - Heatmap for Number of Athletes by Country and Year
st.header("Number of Athletes by Country and Year")
heatmap_data = filtered_data.groupby(['NOC', 'Year']).size().unstack(fill_value=0)
fig_heatmap, ax_heatmap = plt.subplots(figsize=(10, 8))
sns.heatmap(heatmap_data, cmap='viridis', ax=ax_heatmap)
ax_heatmap.set_title(f'Number of Athletes by Country and Year in {sport}')
st.pyplot(fig_heatmap)

# Additional Visualizations can be added here following the same structure.
