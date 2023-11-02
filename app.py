from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data store for reports (you can replace this with a database)
report_store = {}

# Define the /trigger_report API endpoint
@app.route('/trigger_report', methods=['POST'])
def trigger_report():
    # Implement report generation logic here
    # For example, generate a report and store it
    report_id = 'random_report_id'  # Replace with your logic to generate a report and obtain a unique ID
    report_store[report_id] = 'Your generated report data'
    return jsonify({'report_id': report_id})

# Define the /get_report API endpoint
@app.route('/get_report/<report_id>', methods=['GET'])
def get_report(report_id):
    if report_id in report_store:
        return jsonify({'status': 'Complete', 'report_data': report_store[report_id]})
    else:
        return jsonify({'status': 'Running'})

if __name__ == '__main__':
    app.run(debug=True)