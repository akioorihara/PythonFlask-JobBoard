from flask import Flask, render_template, g
import sqlite3

PATH = 'db/jobs.sqlite'

def open_connection():
    connection = getattr(g, '_connection', None)
    if connection == None:
        connection = g._connection = sqlite3.connect(PATH)
    connection.row_factory = sqlite3.Row
    return connection

def execute_sql(sql, values=(), commit=False, single=False):
    connection = open_connection()
    curser = connection.execute(sql, values)
    if commit == True: 
        results = connection.commit()
    else: 
        results = curser.fetchone() if single else curser.fetchall()
    curser.close()
    return results

#@app.teardown_appcontext
def close_connection(exception):
    connection = getattr(g, '_connection', None)
    if connection is not None:
        connection.close()

app = Flask(__name__)

@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')
