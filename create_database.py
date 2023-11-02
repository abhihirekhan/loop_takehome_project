import sqlite3
import csv

# Define the database file path
db_file_path = 'loop.db'

# Define the paths to your CSV files
store_status_csv = 'csvfiles/store_status.csv'
business_hours_csv = 'csvfiles/business_hours.csv'
timezone_csv = 'csvfiles/timezone.csv'

# Define the column names in your CSV files
store_status_columns = ['store_id', 'timestamp_utc', 'status']
business_hours_columns = ['store_id', 'dayOfWeek', 'start_time_local', 'end_time_local']
timezone_columns = ['store_id', 'timezone_str']

# Define a dictionary to map table names to their corresponding CSV files and column names
table_data = {
    'store_status': (store_status_csv, store_status_columns),
    'business_hours': (business_hours_csv, business_hours_columns),
    'timezone': (timezone_csv, timezone_columns)
}

# Connect to the SQLite database
conn = sqlite3.connect(db_file_path)
cursor = conn.cursor()

# Create tables and import data from CSV files
for table_name, (csv_file, columns) in table_data.items():
    # Create the table
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            {', '.join(columns)}
        )
    ''')

    # Import data from the CSV file
    with open(csv_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip the header row
        for row in csv_reader:
            query = f'INSERT INTO {table_name} VALUES ({", ".join(["?"] * len(columns))})'
            cursor.execute(query, row)

# Commit the changes and close the database connection
conn.commit()
conn.close()

print("Database creation and data import completed.")