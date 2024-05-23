import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Đường dẫn tới file Excel
file_path = r"C:\Users\admin\OneDrive\文档\GitHub\Python\Athlete_events.xlsx"

# Tiêu đề của ứng dụng Streamlit
st.title("Olympic Sports Participation in 2016")

# Đọc file Excel
athlete_events = pd.read_excel(file_path)

# Hiển thị một phần dữ liệu để kiểm tra
st.write("Dữ liệu mẫu:", athlete_events.head())

# Định nghĩa các môn thể thao cần chọn
selected_sports = ["Athletics", "Badminton", "Boxing", "Cycling", "Gymnastics", "Swimming"]

# Lọc dữ liệu cho năm 2016 và các môn thể thao đã chọn
my_data = athlete_events[(athlete_events['Year'] == 2016) & (athlete_events['Sport'].isin(selected_sports))]

# Hiển thị dữ liệu đã lọc để kiểm tra
st.write("Dữ liệu đã lọc:", my_data.head())

# Tính toán phân phối phần trăm của từng môn thể thao
sport_counts = my_data['Sport'].value_counts(normalize=True) * 100

# Hiển thị phân phối phần trăm để kiểm tra
st.write("Phân phối phần trăm:", sport_counts)

# Định nghĩa phần nổ cho từng lát trong biểu đồ tròn
explode = [0.02] * len(sport_counts)

# Tạo biểu đồ tròn
fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(sport_counts, labels=sport_counts.index, autopct='%1.1f%%', startangle=140, explode=explode)
ax.axis('equal')  # Tỉ lệ khung hình bằng nhau để đảm bảo biểu đồ tròn

# Hiển thị biểu đồ tròn trong ứng dụng Streamlit
st.pyplot(fig)
