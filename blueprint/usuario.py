#!/usr/bin/python3
import json

from config.mongo import db

from flask import Blueprint,jsonify, request, make_response,Response,render_template
from bson.json_util import dumps as bdumps

#app = flask()
usuario = Blueprint ('usuarios', __name__)


@usuario.route('/usuarios', methods=['GET','POST'])
def usuarios():
    if request.method == 'GET':
        # return Response(bdumps(db.usuarios.find()), content_type='application/json')
        rs = [u for u in db.usuarios.find()] # {'_id': 0} - Caso queira filtrar
        return render_template('usuarios.html',usuarios=rs, title='Usuários')
    else:
        usuario = request.get_json()
        keys= usuario.keys()
        for k in ('nome','email'):
            if k not in keys or not usuario [k].rstrip():
                return make_response(jsonify({'message': 'propridade {} obrigatoria'.format(k)}), 400)
        db.usuarios.insert(usuario)
        return jsonify ({'message': ' usuario cadastrado '})
@usuario.route('/usuarios/delete', methods=['POST'])
def delete_usuarios():
    email = request.args.get('email')
    db.usuarios.remove({'email': email})
    rs = [u for u in db.usuarios.find()] # {'_id': 0} - Caso queira filtrar
    return render_template('usuarios.html', usuarios=rs)

