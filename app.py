import sqlite3
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('clients.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            phone_number TEXT NOT NULL,
            email TEXT NOT NULL,
            address TEXT NOT NULL,
            registration_date TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        full_name = request.form['full_name']
        phone_number = request.form['phone_number']
        email = request.form['email']
        address = request.form['address']
        registration_date = request.form['registration_date']

        conn = sqlite3.connect('clients.db')
        c = conn.cursor()
        c.execute('''
            INSERT INTO clients (full_name, phone_number, email, address, registration_date)
            VALUES (?, ?, ?, ?, ?)
        ''', (full_name, phone_number, email, address, registration_date))
        conn.commit()
        conn.close()

        return redirect(url_for('success'))

    return render_template('index.html')

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=False)
    