import streamlit as st
import sys, os
# Thêm thư mục gốc (Data_visualization) vào path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.db_utils import load_data
from config import NUMERIC_DATA, SAVING_TABLE, VISUAL_DATA, MODEL_DATA

DF = load_data(SAVING_TABLE)
DF_VIS = load_data(VISUAL_DATA)
DF_NUM = load_data(NUMERIC_DATA)
DF_MOD = load_data(MODEL_DATA)


st.title("Tổng quan dữ liệu") 
# Lấy dữ liệu
# Hiển thị bảng và thông tin cơ bản
if st.checkbox("Kích thước dữ liệu:", DF.shape):
    st.write(DF.shape)
    st.dataframe(DF.head(20))

# Hiển thị type of data
if st.checkbox("### Kiểu dữ liệu cột xử lí mỗi null"):
    st.write(DF_VIS.dtypes)
    
if st.checkbox("### Kiểu dữ liệu mỗi cột số"):
    st.write(DF_NUM.dtypes)

if st.checkbox("### Kiểu dữ liệu mỗi cột mô hình"):
    st.write(DF_MOD.dtypes)

# Thống kê mô tả
if st.checkbox("Hiện thống kê mô tả"):
    st.write(DF_NUM.describe())
