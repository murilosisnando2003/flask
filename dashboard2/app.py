#!/usr/bin/python3

from flask import Flask, render_template
from blueprints.pocker import pocker

app = Flask (__name__)
app.register_blueprint(pocker)

@app.route('/')
def home():
	return render_template ('index.html')

app.run()





#docker run --name flask-app -dti -p 9090:80 flask-app   criar um container para ligar em casa