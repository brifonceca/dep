from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<p> hello world!</p>'

@app.route('/api/sensor', methods=['POST'])
def recibir_valores():
    datos = request.json 
    nombres = datos['nombres']
    valor = datos['valor']

    print(f'Mensaje recibido de{request.remote_addr}')
    print(f'Enviado por {nombres}')    
    print(f'valor del sensor: {valor}')
    return 'OK'