import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import sys, os

# Thêm thư mục gốc (Data_visualization) vào path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.db_utils import load_data
from config import SAVING_TABLE

# Load dữ liệu
df = load_data(SAVING_TABLE)

# Chuyển ram sang số nếu cần
df['ram_num'] = df['ram'].str.extract(r'(\d+)').astype(float)

# Tính giá trung bình theo RAM
avg_price = df.groupby('ram_num')['price'].mean().reset_index()

# Vẽ bar chart
plt.figure(figsize=(8,5))
sns.barplot(data=avg_price, x='ram_num', y='price', palette='viridis')
plt.xlabel("RAM (GB)")
plt.ylabel("Giá trung bình")
plt.title("Giá trung bình theo RAM")
plt.xticks(rotation=45)
plt.tight_layout()

# Hiển thị trên Streamlit
st.pyplot(plt)
