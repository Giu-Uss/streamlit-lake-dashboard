import pandas as pd
from sqlalchemy import create_engine

# Database connection details
DB_CONFIG = {
    "dbname": "timeseriesdb",
    "user": "giuseppeussia",
    "password": "Nemo",
    "host": "your_host",
    "port": 5432,
}

def get_timeseries_data(start_date, end_date):
    """Fetch time-series data from PostgreSQL between given dates."""
    engine = create_engine(f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['dbname']}")

    query = f"""
        SELECT time, wsh FROM time_series_data
        WHERE time BETWEEN '{start_date}' AND '{end_date}'
        ORDER BY time;
    """

    df = pd.read_sql(query, engine)
    return df

# Test function
if __name__ == "__main__":
    df = get_timeseries_data("2023-01-01", "2023-12-31")
    print(df.head())  # Print first few rows



