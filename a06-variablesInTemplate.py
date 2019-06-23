#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
from flask import Flask
from flask import render_template # para renderizar template
from math import pow

app = Flask(__name__)
# app = Flask(__name__, template_folder='nueva') # si queremos cambiar la carpeta por deefecto para los templates

@app.route('/user/<name>')
@app.route('/user/')
def user(name= 'Hernan'):
    age = pow(2, 4)
    myList = ['Manzana', 'Mango', 'Pera', 'Papaya', 'Uva']
    return render_template('user.html', nombre=name, age=age, myList=myList) #puedo enviar objetos, clases, diccionarios, tuplas, etc

if __name__ == '__main__':
    app.run(debug=True, port=8001)