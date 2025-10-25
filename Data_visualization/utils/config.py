import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=r"C:\Users\jloy5\OneDrive\Desktop\PricesPhone_Regression\Data_visualization\.env")

print("SERVER:", os.getenv("SERVER"))
print("DATABASE:", os.getenv("DATABASE"))
print("TRACK_TABLE:", os.getenv("TRACK_TABLE"))
print("SAVING_TABLE:", os.getenv("SAVING_TABLE"))

SERVER = os.getenv("SERVER")
DATABASE = os.getenv("DATABASE")
TRACK_TABLE = os.getenv("TRACK_TABLE")
SAVING_TABLE = os.getenv("SAVING_TABLE")

if not all([SERVER, DATABASE, TRACK_TABLE, SAVING_TABLE]):
    raise ValueError("❌ Thiếu cấu hình trong file .env. Vui lòng kiểm tra.")
