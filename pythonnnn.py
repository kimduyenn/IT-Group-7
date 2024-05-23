import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import streamlit as st
import openpyxl
import pandas as pd
import matplotlib.pyplot as plt

athlete_events = pd.read_csv(r'D:\athlete_events.csv')

selected_sports = ["Athletics", "Badminton", "Boxing", "Cycling", "Gymnastics", "Swimming"]
my_data = athlete_events[(athlete_events['Year'] == 2016) & (athlete_events['Sport'].isin(selected_sports))]

sport_counts = my_data['Sport'].value_counts(normalize=True) * 100

explode = [0.02] * len(sport_counts) 

plt.figure(figsize=(8, 8))
plt.pie(sport_counts, labels=sport_counts.index, autopct='%1.1f%%', startangle=140, explode=explode)
plt.axis('equal') 
plt.show()


