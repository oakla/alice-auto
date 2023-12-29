from flask import Flask, render_template, request, jsonify
import pandas as pd
from io import StringIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'csvFile' not in request.files:
        return 'No file uploaded.', 400

    csv_file = request.files['csvFile']

    if csv_file.filename == '':
        return 'No selected file.', 400

    try:
        # Read the CSV file into a pandas DataFrame
        csv_data = pd.read_csv(csv_file)

        # Check if the DataFrame has the expected headers
        expected_headers = ['start', 'end', 'role']
        if not set(expected_headers).issubset(csv_data.columns):
            return 'Invalid CSV headers. Expected: start, end, role', 400

        # Convert DataFrame to JSON
        json_data = csv_data.to_dict(orient='records')

        return jsonify(json_data)

    except Exception as e:
        print(f'Error processing CSV: {e}')
        return 'Error processing CSV. Please try again.', 500

if __name__ == '__main__':
    app.run(debug=True)
