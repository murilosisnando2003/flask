#!/usr/bin/python3


from flask import Flask, jsonify,request,make_response
from datetime import datetime
import json


app = Flask(__name__)

def cont():
    with open('contador','r') as f:
        contador = f.read()
        if not contador: 
            contador = 1
        else:
            contador = int(contador) + 1  
    with open('contador','w') as f:
        f.write("{}".format(contador))     

    return contador


@app.route('/')
def home():
    # print('minha nossa!')
    contador = (cont())
    return jsonify({'status' : 'Running...', 'Count': contador})
    # return json.dumps({'status':' Running...'})

@app.route('/acessos')
def acessos():
         

    date = datetime.now().strftime('%Y-%m-%d %H:%I:%S')
    contador = (cont())
    return jsonify({'Data': date, 'Count' : contador})
       
@app.route('/celular', methods=['POST','GET'])
def celular():
    # return json.dumps(request.get_json())
    retorno = json.dumps({'status' : 'Não encontrado'})
    headers = {'Content-Type' : 'application/json'}
    return make_response(retorno,'Não encontrado', headers)
    
app.run(host='0.0.0.0',debug=True)