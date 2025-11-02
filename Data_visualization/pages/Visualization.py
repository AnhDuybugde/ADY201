import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
from utils.db_utils import load_data
from utils.plot_utils import plot_chart
from Data_visualization.utils.preprocess_data import preprocess_data
from datetime import datetime

st.title("Visualization Dashboard")

# Chọn chế độ xử lý dữ liệu
mode = st.radio(
    "Chọn chế độ xử lý dữ liệu (Processing Mode):",
    ["visual", "numeric", "model"],
    captions=[
        "Visual — chỉ xử lý NaN, dùng cho biểu đồ mô tả (Histogram, Bar, Pie...)",
        "Numeric — ép kiểu số, dùng cho biểu đồ có tính toán (Scatter, Boxplot, Line...)",
        "Model — chuẩn hóa + mã hóa (encode), dùng cho huấn luyện ML hoặc Regression"
    ],
    horizontal=True,
    index=0,
    label_visibility="visible"
)


# --- Load dữ liệu từ DB ---
base_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base_dir, "..", "utils", "processed_data_visual", "visual_data.csv")

df = pd.read_csv(csv_path)
if df is None or df.empty:
    st.warning("Không có dữ liệu để hiển thị.")
    st.stop()

# Tiền xử lý theo mode 
df = preprocess_data(df, mode=mode)
st.success(f"Dữ liệu đã được xử lý theo chế độ: **{mode.upper()}**")
st.write("### Dữ liệu mẫu sau xử lý", df.head())


# Gợi ý biểu đồ phù hợp theo chế độ
chart_options = {
    "visual": ["Histogram", "Bar", "Pie"],
    "numeric": ["Histogram", "Boxplot", "Violin", "Scatter", "Line", "Heatmap (corr)"],
    "model": ["Scatter", "Boxplot", "Violin", "Pairplot", "Heatmap (corr)"]
}

# Chọn loại biểu đồ phù hợp
chart_type = st.selectbox(
    "Chọn loại biểu đồ muốn vẽ:",
    chart_options[mode],
    help=f"Các loại biểu đồ tương thích với chế độ '{mode}'"
)

all_cols = df.columns.tolist()

# Ẩn chọn cột nếu là heatmap
if chart_type == "Heatmap (corr)":
    x_col, y_col = None, None
    st.info("Heatmap sẽ tự động dùng toàn bộ các cột số.")
else:
    x_col = st.selectbox("Chọn cột X:", all_cols)
    y_col = st.selectbox("Chọn cột Y:", all_cols) if chart_type in ["Boxplot", "Scatter", "Bar"] else None

# --- Nút vẽ ---
if st.button("Vẽ biểu đồ"):
    st.session_state["chart_info"] = {"chart_type": chart_type, "x_col": x_col, "y_col": y_col}
    plot_chart(df, x_col, y_col, chart_type)

# --- Nút lưu ---
if "chart_info" in st.session_state:
    info = st.session_state["chart_info"]
    if st.button("Lưu biểu đồ"):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"{info['chart_type']}_{info['x_col']}_{info['y_col'] or 'none'}_{timestamp}.png"
        save_path = os.path.join(os.path.dirname(__file__), '..', 'plots', file_name)
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plot_chart(df, info['x_col'], info['y_col'], info['chart_type'], save_path=save_path)
        st.success(f"Đã lưu biểu đồ tại: `{file_name}`")
