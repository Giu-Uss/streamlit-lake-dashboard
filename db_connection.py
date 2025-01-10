import os
from sqlalchemy import create_engine
import pandas as pd

# Get database credentials from Streamlit Secrets or Environment Variables
DB_CONFIG = {
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),  # Updated host
    "port": os.getenv("DB_PORT", "5432"),
    "sslmode": os.getenv("DB_SSLMODE", "require"),
}

def get_timeseries_data(start_date, end_date):
    """Fetch time-series data from PostgreSQL."""
    try:
        engine = create_engine(
            f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['dbname']}?sslmode={DB_CONFIG['sslmode']}"
        )

        query = f"""
            SELECT time, wsh FROM time_series_data
            WHERE time BETWEEN '{start_date}' AND '{end_date}'
        """

        df = pd.read_sql(query, engine)
        return df

    except Exception as e:
        print(f"Database connection failed: {e}")
        return None

