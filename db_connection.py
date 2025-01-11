import os
from sqlalchemy import create_engine

# Debugging: Print database connection settings
print("DEBUG: DB_HOST =", os.getenv("DB_HOST"))
print("DEBUG: DB_NAME =", os.getenv("DB_NAME"))
print("DEBUG: DB_USER =", os.getenv("DB_USER"))
print("DEBUG: DB_PORT =", os.getenv("DB_PORT"))
print("DEBUG: DB_PASSWORD =", os.getenv("DB_PASSWORD"))

# Database configuration
DB_CONFIG = {
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT", "5432"),
}

# Print the full connection string (without password for security)
connection_url = f"postgresql://{DB_CONFIG['user']}:*****@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['dbname']}"
print(f"DEBUG: Connection URL: {connection_url}")

# Create engine (temporarily disable SSL mode to see if it helps)
engine = create_engine(
    f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['dbname']}?sslmode=disable"
)

# Test connection
try:
    with engine.connect() as connection:
        print("✅ SUCCESS: Connected to the database!")
except Exception as e:
    print("❌ ERROR: Could not connect to the database!")
    print(e)

