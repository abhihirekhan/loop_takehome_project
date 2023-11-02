# Import necessary libraries
import pandas as pd
from datetime import timedelta

# Function to calculate uptime and downtime for a specific store and day
def calculate_uptime_downtime(store_id, day_of_week, status_df, business_hours_df):
    if 'dayOfWeek' in status_df.columns:
        # 'dayOfWeek' column exists, proceed as before
        store_status = status_df[(status_df['store_id'] == store_id) & (status_df['dayOfWeek'] == day_of_week)]
    else:
        # 'dayOfWeek' column is missing, filter by 'store_id' only
        store_status = status_df[status_df['store_id'] == store_id]

    # Filter business hours data for the specific store and day
    business_hours = business_hours_df[(business_hours_df['store_id'] == store_id) & (business_hours_df['dayOfWeek'] == day_of_week)]

    uptime = 0
    downtime = 0

    for index, row in business_hours.iterrows():
        start_time = row['start_time_local']
        end_time = row['end_time_local']

        # Filter status data within the business hours
        business_status = store_status[(store_status['timestamp_utc'].dt.time >= start_time) & (store_status['timestamp_utc'].dt.time <= end_time)]

        # Calculate uptime and downtime within business hours
        for idx, status_row in business_status.iterrows():
            if status_row['status'] == 'active':
                if idx > 0:
                    previous_time = business_status.iloc[idx - 1]['timestamp_utc']
                    time_difference = status_row['timestamp_utc'] - previous_time
                    uptime += time_difference.total_seconds()
            else:
                if idx > 0:
                    previous_time = business_status.iloc[idx - 1]['timestamp_utc']
                    time_difference = status_row['timestamp_utc'] - previous_time
                    downtime += time_difference.total_seconds()

    return uptime, downtime

# Example usage
if __name__ == "__main__":
    # Read your status data and business hours data here
    status_df = pd.read_csv('csvfiles/store_status.csv')
    business_hours_df = pd.read_csv('csvfiles/business_hours.csv')

    # Define the store ID and day of the week for which you want to calculate uptime and downtime
    store_id = 1
    day_of_week = 0  # 0 for Monday, 1 for Tuesday, and so on

    uptime, downtime = calculate_uptime_downtime(store_id, day_of_week, status_df, business_hours_df)

    print(f"Uptime: {uptime / 3600} hours")
    print(f"Downtime: {downtime / 3600} hours")