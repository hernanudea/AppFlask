#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
from flask import Flask
from flask import render_template # para renderizar template
from math import pow

app = Flask(__name__)
# app = Flask(__name__, template_folder='nueva') # si queremos cambiar la carpeta por deefecto para los templates

@app.route('/')
def index():
    name = 'Hernán'
    return render_template('index07.html', name=name)

@app.route('/client')
def client():
    listName = ['Hernán', 'Samuel', 'Matias', 'Eliana']
    return render_template('clients.html', list=listName)

if __name__ == '__main__':
    app.run(debug=True, port=8000)