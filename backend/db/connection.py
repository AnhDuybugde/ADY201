import pyodbc

def get_connection():
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 18 for SQL Server};"
        "SERVER=TRIET\\SQLEXPRESS;"
        "DATABASE=blackmen_restore;"
        "Trusted_Connection=yes;"
        "Encrypt=no;"
    )
    return conn
