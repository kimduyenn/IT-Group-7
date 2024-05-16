import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap

athlete_events = pd.read_csv('Book1.csv')

b_data = athlete_events[athlete_events['Sport'].isin(["Boxing", "Football", "Judo", "Swimming", "Taekwondo"])]

athlete_counts = b_data['Sport'].value_counts().reset_index()
athlete_counts.columns = ['Sport', 'count']

plt.figure(figsize=(8, 8))
plt.pie(athlete_counts['count'], labels=athlete_counts['Sport'], autopct='%1.1f%%', startangle=90, colors=plt.cm.tab10.colors, wedgeprops=dict(width=0.3))
plt.gca().add_patch(plt.Circle((0, 0), 0.5, color='white'))
plt.title('The number of athletes participating in the Olympic during 120 Years')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()





