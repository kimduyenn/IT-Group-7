import streamlit as st
import pandas as pd
import plotly.express as px

# Load your main dataset
data = pd.read_excel('Athlete_events.xlsx')

# Streamlit tabs
tab1, tab2, tab3, tab4 = st.tabs(["Bar Chart", "Box Plot", "Geographic Distribution", "Height and Weight Scatter Plot"])

### TAB 1: BAR CHART
with tab1:
    # Calculate the value counts of Birth_Country
    df = data['Birth_Country'].value_counts()

    # Set the initial value for the slider
    value = 5

    # Get the top N countries with the most prizes
    df1 = df.nlargest(n=value, keep='all')

    # Define color palette for the bars
    color1 = ["#19376D", "#576CBC", "#A5D7E8", "#66347F", "#9E4784", "#D27685", "#D4ADFC", "#F2F7A1", "#FB2576", "#E94560"]

    # Add the slider
    value = tab1.slider("Number of Countries", min_value=1, max_value=10, step=1, value=value)

    # Update the top N countries based on the slider value
    df1 = df.nlargest(n=value, keep='all')
    color1 = color1[:len(df1)]

    # Update the title of the plot
    tab1.subheader("Top {} Countries That Had The Most Olympic Athletes".format(value))

    # Create the bar chart using Altair
    bar_data = pd.DataFrame({"Country": df1.index, "Number of Athletes": df1.values, "Color": color1})
    bars = alt.Chart(bar_data).mark_bar().encode(
        ).properties(width=1400)

    # Rotate x-axis labels for better readability
    bars = bars.configure_axisX(labelAngle=0)

    # Display the chart using Streamlit
    tab1.altair_chart(bars, use_container_width=True)

### TAB 2: BOXPLOT CHART
with tab2:
    # Process the data for the box plot
    data[['Birth_Year', 'Birth_Month', 'Birth_Day']] = data['Birth_Date'].str.split("-", expand=True)
    data[['Death_Day', 'Death_Month', 'Death_Year']] = data['Death_Date'].str.split("/", expand=True)
    data["Birth_Year"] = pd.to_numeric(data["Birth_Year"], errors='coerce')
    data["Death_Year"] = pd.to_numeric(data["Death_Year"], errors='coerce')
    data["Year"] = pd.to_numeric(data["Year"], errors='coerce')
    data['Age'] = data['Death_Year'] - data['Birth_Year']

    # Sort the data by Age in ascending order
    data_sorted = data.sort_values(by='Age', ascending=True)
    # Create a subset of data for Physics, Medicine, and Chemistry categories
    nat = data_sorted[data_sorted['Category'].isin(['Chemistry', 'Physics', 'Medicine'])]
    # Create a subset of data for Literature, Peace, and Economics categories
    soc = data_sorted[data_sorted['Category'].isin(['Literature', 'Peace', 'Economics'])]

    # Create a palette color for categories
    category_colors = {
        'Physics': '#7DEFA1',
        'Chemistry': '#FF2B2B',
        'Medicine': '#A5D7E8',
        'Literature': '#0068C9',
        'Peace': '#D4ADFC',
        'Economics': '#29B09D'
    }

    # Add the title of the plot
    tab2.subheader("Lifespan of Nobel Winners")

    # Store the initial value of widgets in session state
    if "disabled" not in st.session_state:
        st.session_state.disabled = False

    col1, col2, col3 = tab2.columns([2,2,3])
    with col1:
        overview = st.checkbox("Overview of all categories", key="disabled")
        age_type = st.radio("Choose a value you want to look for 👇",
                            ["Oldest age", "Median age", "Youngest age"],
                            key="visibility",
                            disabled= st.session_state.disabled)
    with col2:
        rank = st.selectbox("Rank", ("Maximum", "Minimum"), key="rank",
                            disabled= st.session_state.disabled)
    with col3:
        if overview:
            st.write("Below is all categories.")
        else:
            st.write("Below are all categories with")
            st.write("the {} value of the {} in each group.".format(rank.lower(), age_type.lower()))
            st.write(":green[**Note: Outlier values are accepted.**]")

    # Create a container for displaying the boxplots
    with tab2.container():

        # Define a function to find the category as requested
        def find_category(data, age_type, rank):
            if age_type == "Oldest age":
                if rank == "Maximum":
                    category = data.groupby('Category')['Age'].max().idxmax()
                else:
                    category = data.groupby('Category')['Age'].max().idxmin()
            elif age_type == "Median age":
                if rank == "Maximum":
                    category = data.groupby('Category')['Age'].median().idxmax()
                else:
                    category = data.groupby('Category')['Age'].median().idxmin()
            elif age_type == "Youngest age":
                if rank == "Maximum":
                    category = data.groupby('Category')['Age'].min().idxmax()
                else:
                    category = data.groupby('Category')['Age'].min().idxmin()
            return category

        # Create two columns for displaying the boxplots
        box1, box2 = tab2.columns(2)
        with box1:
            # Add label above the first boxplot
            st.subheader("Natural Sciences")

            # Display the first boxplot
            if overview:
                fig1 = px.box(nat, y="Age", x="Category", color="Category", color_discrete_map=category_colors)
                fig1.update_layout(showlegend=False)  # Remove legend from the first plot
            else:
                nat_cat = find_category(nat, age_type, rank)
                nat_display_cat = nat[nat['Category'].isin([nat_cat])]
                fig1 = px.box(nat_display_cat, y="Age", x="Category", color="Category", color_discrete_map=category_colors)
                fig1.update_layout(showlegend=False)  # Remove legend from the first plot

            st.plotly_chart(fig1, use_container_width=True)

        with box2:
            # Add label above the second boxplot
            st.subheader("Social Sciences")

            # Display the second boxplot
            if overview:
                fig2 = px.box(soc, y="Age", x="Category", color="Category", color_discrete_map=category_colors)
                fig2.update_layout(showlegend=False)  # Remove legend from the second plot
            else:
                soc_cat = find_category(soc, age_type, rank)
                soc_display_cat = soc[soc['Category'].isin([soc_cat])]
                fig2 = px.box(soc_display_cat, y="Age", x="Category", color="Category", color_discrete_map=category_colors)
                fig2.update_layout(showlegend=False)  # Remove legend from the second plot

            st.plotly_chart(fig2, use_container_width=True)

### TAB 3: GEOGRAPHIC DISTRIBUTION CHART
with tab3:
    st.subheader("Geographic Distribution of Olympic Athletes")

    # Group the data by NOC and count the number of athletes
    country_counts = data['NOC'].value_counts().reset_index()
    country_counts.columns = ['NOC', 'Count']

    # Merge with country code data to get latitude and longitude
    country_codes = pd.read_csv('country-list.csv')
    country_counts = country_counts.merge(country_codes, left_on='NOC', right_on='Code', how='left')

    # Create a map with Plotly
    fig = px.scatter_geo(country_counts,
                         locations="Code",
                         hover_name="Country",
                         size="Count",
                         projection="natural earth",
                         title="Geographic Distribution of Olympic Athletes")

    fig.update_layout(title_x=0.5)
    st.plotly_chart(fig, use_container_width=True)

### TAB 4: HEIGHT AND WEIGHT SCATTER PLOT
with tab4:
    st.subheader("Height and Weight of Olympic Athletes")

    # Filter data to remove rows with missing 'Height' or 'Weight'
    data = data.dropna(subset=['Height', 'Weight'])

    # Add a slider to filter data by year
    year_slider = st.slider("Year Range", int(data['Year'].min()), int(data['Year'].max()), (1950, 2020))

    # Filter data by selected year range
    filtered_data = data[(data['Year'] >= year_slider[0]) & (data['Year'] <= year_slider[1])]

    # Create a scatter plot with Plotly
    fig = px.scatter(filtered_data, x='Height', y='Weight', color='Sex',
                     hover_data=['Name', 'Year', 'Sport'],
                     title='Height and Weight of Olympic Athletes')

    fig.update_layout(title_x=0.5)
    st.plotly_chart(fig, use_container_width=True)
