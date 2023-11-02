import requests

# Test /trigger_report API
response = requests.post('http://127.0.0.1:5000/trigger_report')
print(response.json())  # Check the report_id

# Test /get_report API
report_id = response.json()['report_id']
response = requests.get(f'http://127.0.0.1:5000/get_report/{report_id}')
print(response.json())  # Check the report status and data
