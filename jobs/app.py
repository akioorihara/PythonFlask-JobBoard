import flask import Flask, render_template

app = Flash(_name_)

@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')
