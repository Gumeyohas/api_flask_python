from flask import Flask, make_response, jsonify, request
from bd import Carros

# instancia o flask para dentro da variável app
app = Flask(__name__)
app.json.sort_keys = False

@app.route('/carros', methods=['GET'])
def get_lista_carros():
  return make_response(
      jsonify(
        mensagem = 'Lista de carros.',
        dados = Carros
      )
    )

@app.route('/carros/<int:id>', methods=['GET'])
def get_carro(id):
  carro = next((c for c in Carros if c["id"] == id), None)

  return make_response(
      jsonify(
        mensagem = 'Carro retornado com sucesso.',
        carro = carro
      )
    )

@app.route('/carros', methods=['POST'])
def create_carro():
  carro = request.json
  Carros.append(carro)
  return make_response(
      jsonify(
        mensagem = 'Carro cadastrado com sucesso.',
        carro = carro
      )
    )

@app.route('/carros/<int:id>', methods=['DELETE'])
def delete_carro(id):
  carro = next((c for c in Carros if c["id"] == id), None)
  Carros.remove(carro)
  
  return make_response(
      jsonify(
        mensagem = 'Carro deletado da lista.',
        carro = carro
      )
    )

# starta o servidor
app.run()