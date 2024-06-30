import pandas as pd
import streamlit as st
import altair as alt
import plotly.express as px

# Read the data from Excel
data = pd.read_excel('Athlete_events.xlsx')

# Group members information
members_info = [
    {"name": "Tran Thi Thuy Trang", "student_id": "10323060", "email": "10323060@student.vgu.edu.vn", "major": "Finance & Accounting (BFA)"},
    {"name": "Tran Ngoc My Thao", "student_id": "10323059", "email": "10323059@student.vgu.edu.vn", "major": "Finance & Accounting (BFA)"},
    {"name": "Luong Nu Mai Nhung", "student_id": "10323056", "email": "10323056@student.vgu.edu.vn", "major": "Finance & Accounting (BFA)"},
    {"name": "Kim Duyen", "student_id": "10323044", "email": "10323044@student.vgu.edu.vn", "major": "Finance & Accounting (BFA)"}
]

# Set the page configuration
st.set_page_config(page_title="PYTHON 2 - BUSINESS IT 2", page_icon="🥰", layout="wide")

# HEADER SECTION
st.subheader("Hi ❤️ we're from group 7 class afternoon Business IT2")
st.title("What is there more to know about Olympic Athletes?")
st.write("Apart from their achievements, join us today on this app to get to know the athletes' Birth Countries and Average Age of Participation!")

# Display group members information
st.subheader("Group Members:")
for member in members_info:
    st.write(f"- **{member['name']}**: Student ID {member['student_id']}, {member['major']}, Contact email: {member['email']}")

# OUR DATASET
url = "https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results"
st.write("---")
st.header("Our dataset :sparkles:")
st.markdown(f"[Click here to see the original dataset]({url})")
st.write("""
        Our refined data frame contains several main variables as follows:
        - *Name*: Name of the athlete
        - *Sport*: Sport they competed in
        - *Event*: Specific event they participated in
        - *Medal*: Type of medal they won (if any)
        - *NOC*: National Olympic Committee (country) they represented
        - *Age*: Age of the athlete at the time of the event
        - *Height*: Height of the athlete
        - *Weight*: Weight of the athlete
        """)

st.divider()
st.header("Top Birth Countries, Age Distribution, and Geographic Distribution Chart")
st.write("Discover these three graphs below with us")

# Add Sidebar
st.sidebar.write('**🎯 Reporting to Dr. Tan Duc Do**')
st.sidebar.write('**☘️ Members of Group 7 Business IT 2 :**')
for member in members_info:
    st.sidebar.write(member['name'])



### TAB 1: BAR CHART
with tab1:
    # Calculate the value counts of Birth_Country
    df = data['Team'].value_counts()

    # Set the initial value for the slider
    value = 5

    # Get the top N countries with the most participating athletes
    df1 = df.nlargest(n=value, keep='all')

    # Define color palette for the bars
    color1 = ["#19376D", "#576CBC", "#A5D7E8", "#66347F", "#9E4784", "#D27685", "#D4ADFC", "#F2F7A1", "#FB2576", "#E94560"]

    # Add the slider
    value = st.slider("Number of Countries", min_value=1, max_value=10, step=1, value=value)

    # Update the top N countries based on the slider value
    df1 = df.nlargest(n=value, keep='all')
    color1 = color1[:len(df1)]

    # Update the title of the plot
    st.subheader("Top {} Countries That Had The Most Olympic Athletes".format(value))

    # Create the bar chart using Altair
    bar_data = pd.DataFrame({"Country": df1.index, "Number of Athletes": df1.values, "Color": color1})
    bars = alt.Chart(bar_data).mark_bar().encode(
        x=alt.X('Country', sort=None),
        y=alt.Y('Number of Athletes'),
        color=alt.Color('Color', scale=None),
        tooltip=['Country', 'Number of Athletes']
    ).properties(width=1400)

    # Rotate x-axis labels for better readability
    bars = bars.configure_axisX(labelAngle=0)

    # Display the chart using Streamlit
    st.altair_chart(bars, use_container_width=True)

### TAB 2: AGE DISTRIBUTION OVER TIME
with tab2:
    # Filter data to remove rows with missing 'Age' or 'Year'
    data_filtered = data.dropna(subset=['Age', 'Year'])

    # Calculate average age per year
    avg_age_year = data_filtered.groupby('Year')['Age'].mean().reset_index()

    # Plot the line chart
    st.subheader("Average Age of Olympic Athletes Over Time")
    st.write("Explore how the average age of Olympic athletes has changed over the years.")

    # Create the line chart using Plotly
    fig = px.line(avg_age_year, x='Year', y='Age', title='Average Age of Olympic Athletes Over Time')

    # Customize layout and display the plot
    fig.update_traces(mode='lines+markers')
    st.plotly_chart(fig, use_container_width=True)

### TAB 3: GEOGRAPHIC DISTRIBUTION
# Calculate the count of athletes by birth country
athlete_counts = data['NOC'].value_counts().reset_index()
athlete_counts.columns = ['NOC', 'Count']

# Add the title of the plot
tab3.subheader("Geographic Distribution of Olympic Athletes' Birth Countries")

# Create the map visualization
fig_map = px.scatter_geo(
    athlete_counts,
    locations="NOC",
    color="Count",
    hover_name="NOC",
    size="Count",
    projection="natural earth",
    title="Olympic Athletes' Birth Countries",
)

# Display the map
tab3.plotly_chart(fig_map, use_container_width=True)
### TAB 4: HEIGHT AND WEIGHT SCATTER PLOT
with tab4:
    st.subheader("Height and Weight of Olympic Athletes")

    # Filter data to remove rows with missing 'Height' or 'Weight'
    data = data.dropna(subset=['Height', 'Weight'])

    # Add a slider to filter data by year
    year_slider = st.slider("Year Range", int(data['Year'].min()), int(data['Year'].max()), (1950, 2020))

    # Filter data by selected year range
    filtered_data = data[(data['Year'] >= year_slider[0]) & (data['Year'] <= year_slider[1])]

    # Create the scatter plot with Plotly
    fig = px.scatter(filtered_data, 
                     x="Height", 
                     y="Weight", 
                     color="Sex", 
                     hover_data=["Name", "Sport", "Year"],
                     title="Height and Weight of Olympic Athletes")

    fig.update_layout(title_x=0.5)
    st.plotly_chart(fig, use_container_width=True)
