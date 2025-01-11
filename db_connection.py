import os
from sqlalchemy import create_engine
import pandas as pd

# Print debug logs in Streamlit
print("DEBUG: DB_HOST =", os.getenv("DB_HOST"))
import os
from sqlalchemy import create_engine
import pandas as pd

# Print environment variables to verify they are set
print("DEBUG: DB_HOST =", os.getenv("DB_HOST"))
print("DEBUG: DB_NAME =", os.getenv("DB_NAME"))
print("DEBUG: DB_USER =", os.getenv("DB_USER"))
print("DEBUG: DB_PORT =", os.getenv("DB_PORT"))

# Database connection details from environment variables
DB_CONFIG = {
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT", "5432"),
}

# Create the database connection
DATABASE_URL = f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['dbname']}?sslmode=disable"


try:
    engine = create_engine(DATABASE_URL)
    conn = engine.connect()
    print("✅ SUCCESS: Database connected successfully!")
    conn.close()
except Exception as e:
    print("❌ ERROR: Could not connect to the database!")
    print(e)

