import os
from sqlalchemy import create_engine
import pandas as pd

# Debugging: Check if Streamlit is reading the DB_HOST correctly
print("DB_HOST:", os.getenv("DB_HOST"))  

# Database connection details from environment variables
DB_CONFIG = {
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT", "5432"),
}

# Create connection string (ensure sslmode=require is included)
engine = create_engine(
    f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['dbname']}?sslmode=require"
)

