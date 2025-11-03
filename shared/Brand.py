import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import sys, os
import pandas as pd  # Cần import pandas để xử lý DataFrame

# --- Phần giả lập dữ liệu ---
# (Bạn hãy xóa/comment phần này khi dùng code thật với hàm load_data của bạn)
@st.cache_data # Dùng cache để tải data nhanh hơn
def load_data():
    """Hàm giả lập để tạo dữ liệu mẫu."""
    print("Đang tải dữ liệu...") # Thêm để biết khi nào hàm chạy
    data = {
        'ThuongHieu': ['Apple', 'Samsung', 'Apple', 'Xiaomi', 'Samsung', 
                      'Apple', 'Oppo', 'Samsung', 'Xiaomi', 'Realme', 'Apple'],
        'GiaBan': [30, 25, 31, 10, 15, 22, 9, 12, 11, 8, 40]
    }
    return pd.DataFrame(data)
# --- Kết thúc phần giả lập ---


# --- Sử dụng code thật của bạn ---
# Thêm thư mục gốc (Data_visualization) vào path
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# from utils.db_utils import load_data
# ---------------------------------


st.set_page_config(layout="wide")
st.title("📊 Biểu đồ phân tích Thương hiệu")

# Load dữ liệu
df = load_data()

# (Quan trọng) Thay 'ThuongHieu' bằng tên cột chứa thương hiệu thật của bạn
brand_column = 'ThuongHieu' 

if df is not None and not df.empty:
    if brand_column in df.columns:
        st.write(f"### Phân tích số lượng sản phẩm theo '{brand_column}'")
        
        # --- Đây là code vẽ countplot ---
        
        # 1. Tạo Figure và Axes của Matplotlib
        # Đây là cách làm tốt nhất khi dùng Streamlit
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # 2. Dùng Seaborn để vẽ countplot, chỉ định vẽ lên 'ax'
        # Thêm 'order' để sắp xếp các cột từ cao đến thấp
        sns.countplot(
            data=df, 
            x=brand_column, 
            ax=ax,
            order=df[brand_column].value_counts().index,
            palette='viridis'
        )
        
        # 3. Tùy chỉnh biểu đồ (thêm tiêu đề, nhãn)
        ax.set_title('Số lượng mẫu điện thoại theo Thương hiệu', fontsize=16)
        ax.set_xlabel('Thương hiệu', fontsize=12)
        ax.set_ylabel('Số lượng (Count)', fontsize=12)
        
        # Xoay nhãn trục X 45 độ để dễ đọc nếu có nhiều thương hiệu
        ax.tick_params(axis='x', rotation=45)
        
        # Tự động căn chỉnh cho vừa vặn
        plt.tight_layout()
        
        # 4. Hiển thị biểu đồ (Figure 'fig') lên Streamlit
        st.pyplot(fig)
        
        # ---------------------------------

    else:
        st.error(f"Lỗi: Không tìm thấy cột '{brand_column}' trong dữ liệu.")
        st.write("Các cột có sẵn là:", df.columns.tolist())
else:
    st.warning("Không tải được dữ liệu hoặc dữ liệu rỗng.") 