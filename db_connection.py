import os
from sqlalchemy import create_engine
import pandas as pd

# Debugging: Check if Streamlit is reading DB_HOST correctly
print("DEBUG: DB_HOST =", os.getenv("DB_HOST"))

# Database connection details from environment variables
DB_CONFIG = {
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),  # Ensure this is set correctly
    "port": os.getenv("DB_PORT", "5432"),
}

# Ensure the host is correctly formatted
if DB_CONFIG["host"] is None or DB_CONFIG["host"] == "your_host":
    raise ValueError("ERROR: DB_HOST is not set correctly!")

# Create connection string
engine = create_engine(
    f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['dbname']}?sslmode=require"
)

def get_timeseries_data(start_date, end_date):
    """Fetch time-series data from PostgreSQL between given dates."""
    
    query = f"""
        SELECT time, wsh FROM time_series_data
        WHERE time BETWEEN '{start_date}' AND '{end_date}'
    """
    
    df = pd.read_sql(query, engine)
    return df

