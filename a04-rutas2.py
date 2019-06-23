from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hola Mundo'

@app.route('/saludo')
def saludo():
    return 'Hola Mundo desde función saludo!'

#para tutas de la forma params/123/Hernan Velasquez
@app.route('/params/<id>/<int:sueldo>') # valida el tipo de dato
@app.route('/params/')
def params(id='sin valor', sueldo=0):
    return 'El ID es [{}] y el nombre es: [{}]!'.format(id, sueldo)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
