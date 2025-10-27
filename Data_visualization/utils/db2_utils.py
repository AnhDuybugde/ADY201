# File: utils/db_utils.py

import pyodbc
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
from config import SAVING_TABLE, SERVER, DATABASE
import os

# Load biến môi trường từ file .env
load_dotenv()

def get_connection():
    conn = pyodbc.connect(
        f"DRIVER={{ODBC Driver 18 for SQL Server}};"
        f"SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;Encrypt=no;"
    )
    return conn, conn.cursor()

def create_table_if_not_exists(cursor, table_name=SAVING_TABLE):
    query = f"""
    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='{table_name}' AND xtype='U')
    CREATE TABLE {table_name} (
        product_id NVARCHAR(50) PRIMARY KEY,
        brand NVARCHAR(100),
        os NVARCHAR(MAX),
        ram NVARCHAR(100),
        rom NVARCHAR(100),
        battery NVARCHAR(MAX),
        camera_primary NVARCHAR(MAX),
        camera_secondary NVARCHAR(MAX),
        chipset NVARCHAR(100),
        gpu NVARCHAR(100),
        display_size NVARCHAR(50),
        screen NVARCHAR(MAX),
        sensor NVARCHAR(MAX),
        watt NVARCHAR(MAX),
        nfc NVARCHAR(50),
        jack_support NVARCHAR(50),
        price FLOAT
    )
    """
    cursor.execute(query)
