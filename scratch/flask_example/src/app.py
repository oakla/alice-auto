from flask import Flask, render_template, request, jsonify, redirect
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Function to create a table if it doesn't exist
def create_table():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS form_entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            date TEXT NOT NULL,
            option TEXT NOT NULL
        )
    ''')

    connection.commit()
    connection.close()

create_table()

# def connect_db():
#     return sqlite3.connect(app.config['DATABASE'])


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        date = request.form['date']
        option = request.form['option']

        # Insert data into the table
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO form_entries (name, date, option)
            VALUES (?, ?, ?)
        ''', (name, date, option))
        connection.commit()
        connection.close()

        return redirect('/')
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)



@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"