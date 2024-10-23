from flask import Flask

app=Flask(__name__)

@app.route('/')

def home():
    return "Demo Flask App"

@app.route('/demo/<name>')
def demo(name):
    return "Demo"+name

app.run(debug=True)