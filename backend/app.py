from flask import Flask, redirect # type: ignore
from utils.response import json

app = Flask(__name__)
default_route = '/api/v1/'

@app.route("/")
def checker():
    return redirect(default_route)

@app.route(default_route)
def index():
    return json(True, 'Welcome to the API', 200)
  
if __name__ == '__main__':
    app.run(debug=True)