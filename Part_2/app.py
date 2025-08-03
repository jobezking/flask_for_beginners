'''
#To run app
export FLASK_APP=app.py
export FLASK_ENV=development
flask run --host=0.0.0.0 --port=8080
#should see Running on http://127.0.0.1:5000 which you should open on your browser
'''

from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Welcome to our homepage<h1>
    
@app.route('/about')
def home():
    return '<p>About us: Jesus Christ Is Lord<p>
    
@app.route('/contact')
def home():
    return '<p>Contact us at hello@example.com<p>