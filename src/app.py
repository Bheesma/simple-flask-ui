
from flask import Flask,render_template

app =  Flask(__name__)

#------------------------------------------------------------

@app.route('/')
def index():
    greeting="Hello World - Simple Flask UI !!!"
    return render_template('index.html', greet=greeting)

#------------------------------------------------------------

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

#------------------------------------------------------------

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

#------------------------------------------------------------

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)