from flask import render_template
from core import app

@app.route('/')
def index():
    greeting="Hello World - Simple Flask UI !!!"
    return render_template('index.html', greet=greeting)
