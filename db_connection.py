import os
from sqlalchemy import create_engine
import pandas as pd

# Print debug logs in Streamlit
print("DEBUG: DB_HOST =", os.getenv("DB_HOST"))
print("DEBUG: DB_NAME =", os.getenv("DB_NAME"))
print("DEBUG: DB_USER =", os.getenv("DB_USER"))
print("DEBUG: DB_PORT =", os.getenv("DB_PORT"))

# Database configuration
DB_CONFIG = {
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT", "5432"),
}

# Print the full connection string for debugging
print(f"DEBUG: Connection string -> postgresql://{DB_CONFIG['user']}:********@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['dbname']}")

# Create engine
engine = create_engine(
    f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['dbname']}?sslmode=require"
)

