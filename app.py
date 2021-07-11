from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
import requests
import json
import omdb 

app = Flask(__name__)
api_key="b7f7cd9a"
omdb.set_default('apikey', api_key)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/results", methods=["POST"])
def results():
    title = request.form["moviesearch"]
    r = requests.get('http://www.omdbapi.com/?apikey='+api_key+'&s='+title)
    movieList= r.json()['Search']
    return render_template('results.html',movieList=movieList)

if __name__ == '__main__':
    app.run(debug=True)