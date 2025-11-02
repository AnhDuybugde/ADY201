import streamlit as st
import sys, os
# Thêm thư mục gốc (Data_visualization) vào path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.db_utils import get_data

st.title("Tổng quan dữ liệu") 
# Lấy dữ liệu
df = get_data()

# Hiển thị bảng và thông tin cơ bản
st.write("Kích thước dữ liệu:", df.shape)
st.dataframe(df.head(20))

# Thống kê mô tả
if st.checkbox("Hiện thống kê mô tả"):
    st.write(df.describe())

# streamlit run C:/Users/jloy5/OneDrive/Desktop/PricesPhone_Regression/Data_visualization/pages/Data_overview.py
