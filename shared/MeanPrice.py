import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import sys, os
import pandas as pd  # Cần import pandas để xử lý DataFrame
import numpy as np   # Cần cho Barplot (tính trung bình)

# --- Phần giả lập dữ liệu ---
# (Bạn hãy xóa/comment phần này khi dùng code thật với hàm load_data của bạn)
@st.cache_data # Dùng cache để tải data nhanh hơn
def load_data():
    """Hàm giả lập để tạo dữ liệu mẫu."""
    print("Đang tải dữ liệu...") # Thêm để biết khi nào hàm chạy
    data = {
        'ThuongHieu': ['Apple', 'Samsung', 'Apple', 'Xiaomi', 'Samsung', 
                       'Apple', 'Oppo', 'Samsung', 'Xiaomi', 'Realme', 'Apple',
                       'Samsung', 'Xiaomi', 'Oppo'],
        'GiaBan': [30, 25, 31, 10, 15, 22, 9, 12, 11, 8, 40, 28, 13, 10]
    }
    return pd.DataFrame(data)
# --- Kết thúc phần giả lập ---


# --- Sử dụng code thật của bạn ---
# Thêm thư mục gốc (Data_visualization) vào path
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# from utils.db_utils import load_data
# ---------------------------------


st.set_page_config(layout="wide")
st.title("📊 Phân tích Giá Bán Trung Bình theo Thương hiệu")

# Load dữ liệu
df = load_data()

# (Quan trọng) Thay 'ThuongHieu' và 'GiaBan' bằng tên cột thật của bạn
brand_column = 'ThuongHieu' 
price_column = 'GiaBan'

if df is not None and not df.empty:
    if brand_column in df.columns and price_column in df.columns:
        
        # --- Biểu đồ Barplot (Biểu đồ cột thể hiện GIÁ TRUNG BÌNH) ---
        st.subheader("Giá Bán TRUNG BÌNH theo Thương hiệu")
        st.info("Biểu đồ này hiển thị giá bán trung bình (mean) cho từng thương hiệu.")
        
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(
            data=df, 
            x=brand_column, 
            y=price_column,
            ax=ax,
            estimator=np.mean, # Tính trung bình (đây là mặc định)
            palette='plasma' # Dùng màu 'plasma'
        )
        
        ax.set_title('Giá Bán Trung Bình theo Thương hiệu', fontsize=16)
        ax.set_xlabel('Thương hiệu', fontsize=12)
        ax.set_ylabel('Giá Bán Trung Bình', fontsize=12)
        ax.tick_params(axis='x', rotation=45)
        plt.tight_layout()
        st.pyplot(fig)

    else:
        st.error(f"Lỗi: Không tìm thấy cột '{brand_column}' hoặc '{price_column}' trong dữ liệu.")
        st.write("Các cột có sẵn là:", df.columns.tolist())
else:
    st.warning(" Không tải được dữ liệu hoặc dữ liệu rỗng.")

