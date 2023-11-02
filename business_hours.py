import pandas as pd
from pytz import timezone

# Read the business hours data
business_hours_df = pd.read_csv('csvfiles/business_hours.csv')

# Read the timezones data
timezones_df = pd.read_csv('csvfiles/timezones.csv')

# Assuming you have a function to convert time zones
def convert_to_local_time(timestamp_utc, timezone_str):
    local_timezone = timezone(timezone_str)
    return timestamp_utc.astimezone(local_timezone)

# Create a dictionary to store store_id to business hours mapping
store_business_hours = {}

# Iterate through business hours data and timezones data to determine business hours
for index, row in business_hours_df.iterrows():
    store_id = row['store_id']
    day_of_week = row['dayOfWeek']
    start_time_utc = convert_to_local_time(row['start_time_local'], timezones_df[timezones_df['store_id'] == store_id]['timezone_str'].values[0])
    end_time_utc = convert_to_local_time(row['end_time_local'], timezones_df[timezones_df['store_id'] == store_id]['timezone_str'].values[0])

    # Store business hours for each store and day of the week
    if store_id not in store_business_hours:
        store_business_hours[store_id] = {}
    store_business_hours[store_id][day_of_week] = (start_time_utc, end_time_utc)

# store_business_hours is now a dictionary containing the business hours for each store and day of the week