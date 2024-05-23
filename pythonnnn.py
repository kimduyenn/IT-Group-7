import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import streamlit as st
import openpyxl

athlete_events = pd.read_excel(r"C:\Users\admin\OneDrive\文档\GitHub\Python\Athlete_events.xlsx")

# PLOT 1
selected_sports = ["Athletics", "Badminton", "Boxing", "Cycling", "Gymnastics", "Swimming"]
my_data = athlete_events[(athlete_events['Year'] == 2016) & (athlete_events['Sport'].isin(selected_sports))]

sport_counts = my_data['Sport'].value_counts(normalize=True) * 100

explode = [0.02] * len(sport_counts) 

plt.figure(figsize=(8, 8))
plt.pie(sport_counts, labels=sport_counts.index, autopct='%1.1f%%', startangle=140, explode=explode)
plt.axis('equal') 
plt.show()


# PLOT 2
Year2014 = athlete_events[athlete_events['Year'] == 2014]

Teams = ["United States", "Russia", "Norway", "Germany", "Canada"]

m_data = Year2014[Year2014['Team'].isin(Teams)]

m_data_unique = m_data.drop_duplicates(subset='Name', keep='first')
team_counts = m_data_unique['Team'].value_counts().reset_index()
team_counts.columns = ['Team', 'Count']
team_counts = team_counts.sort_values(by='Count', ascending=False)

unique_colors = ["#FF5733", "#FFBD33", "#33FF57", "#33FFBD", "#5733FF"]

plt.figure(figsize=(10, 6))
bars = plt.barh(team_counts['Team'], team_counts['Count'], color=unique_colors, alpha=0.8)

average_width = team_counts['Count'].mean()
for i, bar in enumerate(bars):
 plt.text(bar.get_width(), bar.get_y() + bar.get_height()/2, int(bar.get_width()), ha='left', va='center', color='black', fontsize=12)

plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.title("The number of athletes participating from five countries in the 2014 Winter Olympics")
plt.xlabel("Athletes")
plt.ylabel("Countries")

plt.show()

# PLOT 3
filtered_data = athlete_events[(athlete_events['Year'] >= 1990) & (athlete_events['Year'] <= 2016)]
filtered_data = filtered_data.dropna(subset=['Sex'])

yearly_gender_counts = filtered_data.groupby(['Year', 'Sex']).size().unstack(fill_value=0)

yearly_gender_counts['Total'] = yearly_gender_counts['M'] + yearly_gender_counts['F']
yearly_gender_counts.sort_values(by='M', inplace=True)

plt.figure(figsize=(10, 6))
colors = {'M': '#FF6666', 'F': '#FF9966'}

plt.bar(yearly_gender_counts.index, yearly_gender_counts['M'], color=colors['M'], label='Male')
for i, count in enumerate(yearly_gender_counts['M']):
  plt.text(yearly_gender_counts.index[i], count, str(count), ha='center', va='bottom', color='black', fontsize=8)

plt.bar(yearly_gender_counts.index, yearly_gender_counts['F'], bottom=yearly_gender_counts['M'], color=colors['F'], label='Female')
for i, count in enumerate(yearly_gender_counts['F']):
  plt.text(yearly_gender_counts.index[i], count + yearly_gender_counts['M'].iloc[i], str(count), ha='center', va='bottom', color='black', fontsize=8)

plt.xlabel("Year")
plt.ylabel("Number of Athletes")
plt.title("Number of Athletes by Gender (1990-2016)")
plt.legend(title='Sex', labels=['Male', 'Female'])
plt.grid(axis='y', linestyle='--', alpha=0.1)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.xticks(yearly_gender_counts.index)
plt.tight_layout()
plt.show()

# PLOT 4
b_data = athlete_events[athlete_events['Sport'].isin(["Boxing", "Football", "Judo", "Swimming", "Taekwondo"])]
athlete_counts = b_data['Sport'].value_counts().reset_index()
athlete_counts.columns = ['Sport', 'count']

plt.figure(figsize=(8, 8))
plt.pie(athlete_counts['count'], labels=athlete_counts['Sport'], autopct='%1.1f%%', startangle=90, colors=plt.cm.tab10.colors, wedgeprops=dict(width=0.3))
plt.gca().add_patch(plt.Circle((0, 0), 0.5, color='white'))
plt.title('The number of athletes participating in the Olympic during 120 Years')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()

# PLOT 5
filtered_dat = athlete_events[(athlete_events['Season'] == "Summer") & (athlete_events['Year'] >= 1990) & (athlete_events['Year'] <= 2016)]
filtered_dat = filtered_dat[['Weight', 'Sex']].dropna()
filtered_dat['Weight'] = pd.to_numeric(filtered_dat['Weight'])
fig, axs = plt.subplots(1, 2, figsize=(14, 6))
axs[0].hist(filtered_dat[filtered_dat['Sex'] == 'M']['Weight'], bins=range(0, 300, 5), color="#1f77b4", edgecolor='white', alpha=1, label='Male', density=False)
axs[0].set_xlabel('Weight (kg)')
axs[0].set_ylabel('Number of Athletes')
axs[0].legend()
axs[0].grid(True, linestyle='--', alpha=0.7)
axs[1].hist(filtered_dat[filtered_dat['Sex'] == 'F']['Weight'], bins=range(0, 300, 5), color="#E54646", edgecolor='white', alpha=1, label='Female', density=False)
axs[1].set_xlabel('Weight (kg)')
axs[1].legend()
axs[1].grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# PLOT 6
import numpy as np

filtered_dat = athlete_events[athlete_events['Year'] >= 1990]
filtered_dat = filtered_dat[['Year', 'Season', 'Sport']].drop_duplicates()

sports_count = filtered_dat.groupby(['Year', 'Season']).size().unstack(fill_value=0)
fig, axs = plt.subplots(2, 1, figsize=(12, 12))

years = sports_count.index
summer_counts = sports_count['Summer']
bar_width = 0.35
x = np.arange(len(years))

axs[0].bar(x, summer_counts, width=bar_width, color='#FFA500', alpha=0.7, label='Summer')
axs[0].set_xlabel('Year')
axs[0].set_ylabel('Number of Sports')
axs[0].set_title('Number of Sports Participated in Summer Season (1990-2022)')
axs[0].set_xticks(x)
axs[0].set_xticklabels(years)
axs[0].legend()
axs[0].grid(True, linestyle='-', alpha=0.2)

for i, summer_count in enumerate(summer_counts):
  axs[0].text(x[i], summer_count, str(summer_count), ha='center', va='bottom', fontsize=12)


winter_counts = sports_count['Winter']

axs[1].bar(x, winter_counts, width=bar_width, color='#4682B4', alpha=0.7, label='Winter')
axs[1].set_xlabel('Year')
axs[1].set_ylabel('Number of Sports')
axs[1].set_title('Number of Sports Participated in Winter Season (1990-2022)')
axs[1].set_xticks(x)
axs[1].set_xticklabels(years)
axs[1].legend()
axs[1].grid(True, linestyle='-', alpha=0.2)

for i, winter_count in enumerate(winter_counts):
  axs[1].text(x[i], winter_count, str(winter_count), ha='center', va='bottom', fontsize=12)

plt.tight_layout()
plt.show()


# PLOT 7
year2002 = athlete_events[athlete_events['Year'] == 2002]

year2002['Age'] = pd.to_numeric(year2002['Age'], errors='coerce')

year2002_count = year2002.drop_duplicates(subset=['ID', 'Age', 'Sex'])

year2002_count = year2002_count.groupby(['Age', 'Sex']).size().reset_index(name='count')

plt.figure(figsize=(10, 6))

for sex, color in zip(['M', 'F'], ['red', 'blue']):
 data = year2002_count[year2002_count['Sex'] == sex]
 plt.fill_between(data['Age'], data['count'], color=color, alpha=0.35, label=sex)

plt.xlabel('Age')
plt.ylabel('Athletes')
plt.title('Density Chart with Athlete Count by Age and Sex in 2002')
plt.legend(title='Sex')
plt.grid(True, linestyle='--', alpha=0.3)
plt.tight_layout()
plt.show()


# PLOT 8
filtered_dat = athlete_events[(athlete_events['Year'] >= 1990) & (athlete_events['Year'] <= 2016)]

summary_dat = filtered_dat.groupby(['Year', 'Season']).size().reset_index(name='total_athletes')
plt.figure(figsize=(10, 6))

for season, color in zip(['Summer', 'Winter'], ['darkorange', 'steelblue']):
 data = summary_dat[summary_dat['Season'] == season]
 plt.plot(data['Year'], data['total_athletes'], marker='o', linestyle='-', color=color, label=season)
 for i, row in data.iterrows():
  plt.text(row['Year'], row['total_athletes'], str(row['total_athletes']), ha='center', va='bottom', fontsize=15)

plt.xlabel('Year', fontsize=14)
plt.ylabel('Total Athletes', fontsize=14)
plt.title('Total Athletes in Summer and Winter (1992-2016)', fontsize=16)
plt.legend(title='Season', fontsize=12, loc='center left', bbox_to_anchor=(1, 0.5), ncol=1)
plt.grid(True, linestyle='--', alpha=0.25)
plt.xticks(range(1990, 2017, 2), fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()
plt.show()

# PLOT 9 
import seaborn as sns

selected_sports = ["Basketball", "Gymnastics", "Swimming", "Athletics", "Boxing", "Wrestling"]
sport_age = athlete_events[(athlete_events['Year'] >= 1960) & (athlete_events['Year'] <= 2000) & athlete_events['Sport'].isin(selected_sports)]

sport_age['Year'] = pd.to_numeric(sport_age['Year'])
sport_age['Age'] = pd.to_numeric(sport_age['Age'], errors='coerce')

sport_medians = sport_age.groupby('Sport')['Age'].median().sort_values().index

plt.figure(figsize=(12, 8))
sns.boxplot(data=sport_age, x='Sport', y='Age', order=sport_medians, palette=sns.color_palette("Paired")) 
plt.xticks(ha='center', fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel('Sport', fontsize=14)
plt.ylabel('Age', fontsize=14)
plt.title('Distribution of Age by Sport (1960-2000)', fontsize=16)

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()



# PLOT 10 
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import cartopy.crs as ccrs
import cartopy.feature as cfeature

east_asian_countries = [
    "China", "Japan", "South Korea", "North Korea", "Taiwan", "Hong Kong", "Mongolia", "Macau", "Vietnam", "Laos", "Cambodia", "Thailand", "Myanmar", "Malaysia", "Singapore", "Brunei", "Philippines", "Indonesia", "Timor-Leste"]

world_map = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

east_asian_map = world_map[world_map['name'].isin(east_asian_countries)]

athlete_counts = athlete_events[
    (athlete_events['Team'].isin(east_asian_countries)) &(athlete_events['Year'].between(1990, 2016))].groupby('Team')['ID'].nunique().reset_index(name='athlete_count')

east_asian_map_with_athletes = east_asian_map.merge(athlete_counts, left_on='name', right_on='Team', how='left')

east_asian_map_with_athletes['athlete_count'] = east_asian_map_with_athletes['athlete_count'].fillna(0)

fig, ax = plt.subplots(figsize=(10, 6), subplot_kw={'projection': ccrs.PlateCarree()})
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':')
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)

colors = ['#FFFFFF', '#00CCFF', '#0099FF', '#0066FF', '#0033CC', '#000099']
cmap = LinearSegmentedColormap.from_list('custom', colors, N=2500)

east_asian_map_with_athletes.boundary.plot(ax=ax, linewidth=1, edgecolor='black')
east_asian_map_with_athletes.plot(column='athlete_count', cmap=cmap, linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)

for idx, row in east_asian_map_with_athletes.iterrows():
    if pd.notna(row['athlete_count']):
        plt.text(row.geometry.centroid.x, row.geometry.centroid.y, row['name'], 
                 ha='center', fontsize=8, color='red', transform=ccrs.PlateCarree())

ax.set_title('Number of Athletes in East Asian Countries (1990-2016)', fontsize=14)

plt.tight_layout()
plt.show()
