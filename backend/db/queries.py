import sys, os

# Thêm đường dẫn tới thư mục backend để tránh lỗi ModuleNotFoundError
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db.connection import get_connection


def fetch_all_phones():
    """Lấy toàn bộ dữ liệu từ bảng Phones_Numeric_Data"""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * 
        FROM dbo.Phones_Numeric_Data
    """)

    # Lấy tên cột
    columns = [col[0] for col in cursor.description]
    # Gộp cột và dữ liệu thành danh sách dict
    data = [dict(zip(columns, row)) for row in cursor.fetchall()]

    cursor.close()
    conn.close()
    return data


# ✅ Dùng để test riêng lẻ file này (chạy trực tiếp queries.py)
if __name__ == "__main__":
    phones = fetch_all_phones()
    print(f"Tổng số điện thoại: {len(phones)}")
    for p in phones[:5]:  # in 5 dòng đầu tiên
        print(p)
