import streamlit as st
import sys, os
# Thêm thư mục gốc (Data_visualization) vào path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.db_utils import load_data
from config import NUMERIC_DATA, SAVING_TABLE

st.title("Tổng quan dữ liệu") 
# Lấy dữ liệu
df = load_data(SAVING_TABLE)
# Hiển thị bảng và thông tin cơ bản
st.write("Kích thước dữ liệu:", df.shape)
st.dataframe(df.head(20))
    
DF_NUM = load_data(NUMERIC_DATA)
# Thống kê mô tả
if st.checkbox("Hiện thống kê mô tả"):
    st.write(DF_NUM.describe())
