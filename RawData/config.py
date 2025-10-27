# src/config.py
import os
import pyodbc
from dotenv import load_dotenv

# Tự động load .env ở thư mục gốc
load_dotenv()

SERVER = os.getenv("SERVER")
DATABASE = os.getenv("DATABASE")
TABLE_NAME = os.getenv("TABLE_NAME")

URL = os.getenv("URL")
CATEGORY_ID = os.getenv("CATEGORY_ID")
PROVINCE_ID = int(os.getenv("PROVINCE_ID"))
MAX_PAGES = int(os.getenv("MAX_PAGES"))
HEADERS = {"Content-Type": "application/json", "User-Agent": os.getenv("USER_AGENT")}

def get_connection():
    conn_str = f"Driver={{SQL Server}};Server={SERVER};Database={DATABASE};Trusted_Connection=yes;"
    return pyodbc.connect(conn_str)
