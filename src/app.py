
from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    greeting="Hello World - Simple Flask UI !!!"
    return render_template('index.html', greet=greeting)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)