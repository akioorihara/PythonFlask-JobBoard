from flask import Flask, render_template, g
import sqlite3

PATH = 'db/jobs.sqlite'

def open_connection()
 getattr()

app = Flask(__name__)

@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')
