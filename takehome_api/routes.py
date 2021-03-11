from takehome_api import app, db
from flask import render_template, jsonify

from takehome_api.models import Divvy


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/duration/<starttime>/<stoptime>', methods=['GET'])
def duration(starttime, stoptime):
    query = Divvy.query.filter(
        Divvy.starttime.like(starttime),
        Divvy.stoptime.like(stoptime)
    ).all()
    print(query)
    return f'Trip Duration = {query[0]}'
