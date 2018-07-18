#!/usr/bin/python3
from flask import Flask, jsonify,render_template
from blueprint.usuario import usuario

app = Flask(__name__)
app.register_blueprint(usuario)

@app.route('/')
def home():
    # print('minha nossa!')
    # contador = (cont())
    return render_template('index.html')
    # return json.dumps({'status':' Running...'})


if __name__ =='__main__':    
    app.run(host='0.0.0.0',debug=True)