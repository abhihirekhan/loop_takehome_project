import pandas as pd

# Step 1: Read Data from CSV Files

# Read the store status data
store_status_df = pd.read_csv('csvfiles/store_status.csv')

# Read the business hours data
business_hours_df = pd.read_csv('csvfiles/business_hours.csv')

# Read the timezones data
timezones_df = pd.read_csv('csvfiles/timezones.csv')

# Step 2: Data Cleaning and Preprocessing

# Convert timestamp columns to datetime objects
store_status_df['timestamp_utc'] = pd.to_datetime(store_status_df['timestamp_utc'])

# Ensure consistent datetime format for business hours data
business_hours_df['start_time_local'] = pd.to_datetime(business_hours_df['start_time_local'])
business_hours_df['end_time_local'] = pd.to_datetime(business_hours_df['end_time_local'])

# Handle missing data as specified in the project requirements
# For example, assume stores are open 24/7 if data is missing in business_hours_df
business_hours_df.fillna({'start_time_local': pd.Timestamp('00:00:00'), 'end_time_local': pd.Timestamp('23:59:59')}, inplace=True)

# Step 3: Print Sample Data to Check

# Print the first few rows of each dataframe to verify data loading and preprocessing
print("Store Status Data:")
print(store_status_df.head())

print("\nBusiness Hours Data:")
print(business_hours_df.head())

print("\nTimezones Data:")
print(timezones_df.head())