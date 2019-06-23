from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hola Mundo'

@app.route('/saludo')
def saludo():
    return 'Hola Mundo desde función saludo!'

# para manejar parametros, necesitamos la segunda libreria
# http://localhost:8000/params?name=Hernan%20Velasquez&id=132
@app.route('/params')
def params():
    id = request.args.get('id', 'sin id')
    name = request.args.get('name', 'sin name')
    return 'El ID es [{}] y el nombre es: [{}]!'.format(id, name)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
