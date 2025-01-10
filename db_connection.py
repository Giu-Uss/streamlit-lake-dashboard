import os
from sqlalchemy import create_engine
import pandas as pd
print("DB_HOST:", os.getenv("DB_HOST"))  # Debugging: Check Streamlit is reading this correctly

# Database connection details from environment variables
DB_CONFIG = {
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT", "5432"),
}

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

