from flask import Flask, render_template, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.config['DATABASE'] = 'timeslots.db'

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with app.app_context():
        db = connect_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


# *** NEW CODE FOR DB DISPLAY ***

# Function to fetch all tables in the database
def get_tables():
    connection = sqlite3.connect('timeslots.db')
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    connection.close()
    return tables

# Function to fetch all rows from a specific table
def get_table_data(table_name):
    connection = sqlite3.connect('timeslots.db')
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {table_name};")
    data = cursor.fetchall()
    column_names = [description[0] for description in cursor.description]
    connection.close()
    return column_names, data

@app.route('/')
def index():
    tables = get_tables()
    return render_template('index.html', tables=tables)

@app.route('/display')
def display():
    tables = get_tables()
    table_data = {}
    for table in tables:
        table_name = table[0]
        column_names, data = get_table_data(table_name)
        table_data[table_name] = {'column_names': column_names, 'data': data}
    return render_template('display.html', table_data=table_data)

# END
# **** OTHERE METHOD TO VIEW TABLES ****
@app.route('/table/<table_name>')
def view_table(table_name):
    column_names, data = get_table_data(table_name)
    return render_template('table.html', table_name=table_name, column_names=column_names, data=data)
# END

# **** NEW CODE FOR BULK DATA SUBMISSION ****
@app.route('/insert_data', methods=['POST'])
def insert_data():
    try:
        data = request.get_json()['data']

        # Connect to SQLite database (create a new one if not exists)
        conn = sqlite3.connect('timeslots.db')
        cursor = conn.cursor()

        # Create the table if not exists
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS time_slots (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                start_datetime TEXT,
                end_datetime TEXT,
                role TEXT
            )
        ''')

        # Insert data into the database
        for row in data:
            cursor.execute('''
                INSERT INTO time_slots (start_datetime, end_datetime, role)
                VALUES (?, ?, ?)
            ''', (row[0], row[1], row[2]))

        # Commit the changes and close the connection
        conn.commit()
        conn.close()

        response = {'message': 'Data inserted successfully'}
    except Exception as e:
        response = {'message': f'Error: {str(e)}'}

    return jsonify(response)



# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/add_time_slots', methods=['POST'])
def add_time_slots():
    try:
        start_datetime = request.form['startDateTime']
        end_datetime = request.form['endDateTime']
        role = request.form['role']
        duration = float(request.form['duration'])

        db = connect_db()
        cur = db.cursor()
        cur.execute(
            "INSERT INTO time_slots (start_datetime, end_datetime, role, duration) VALUES (?, ?, ?, ?)",
            (start_datetime, end_datetime, role, duration)
        )
        db.commit()

        return jsonify({'message': 'Data written to the database successfully!'})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
