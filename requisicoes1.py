#!/usr/bin/python3

import requests

#headers = {'Content-Type' : 'application/json'}
#data = {"nome" : "Pedro", "email" : "mamada@ig.com.br"}
# data = {"nome": " Leonardo"}

#response = requests.get('http://phpypesh.com.br')
response = requests.get('http://127.0.0.1:5000/usuarios')
data = response.json()
print('{0:.>10}{1:.>30}'.format('ID','NOME',))
for bunda in data['usuarios']:
    x = bunda['id']
    if x % 2 == 0:
        print('{0:.>10}{1:.>30}'.format(bunda['id'],bunda['nome']))
