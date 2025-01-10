import os
from sqlalchemy import create_engine
import pandas as pd

# Database connection details
DB_CONFIG = {
    "dbname": "streamlit_lake_db",
    "user": "streamlit_lake_db_user",
    "password": "NJTV4XbHoPxo4iYnrcIHOf2V3gvuuC9R",
    "host": "dpg-cu0lj0pu0jms73dsdqh0-a",
    "port": 5432,
}

def get_timeseries_data(start_date, end_date):
    """Fetch time-series data from PostgreSQL between given dates."""
    engine = create_engine(f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['dbname']}?sslmode=require")
    
    query = f"""
        SELECT time, wsh FROM time_series_data
        WHERE time BETWEEN '{start_date}' AND '{end_date}'
    """
    
    df = pd.read_sql(query, engine)
    return df

