from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {'id': 0, 'nome': 'Hercules', 'Habilidades': ['Python', 'Machine Learning', 'Flask', 'Rest API', 'Ciencia de dados']},
    {'id': 1, 'nome': 'kira', 'Habilidades': ['Python', 'Flask', 'Rest API']},
    {'id': 2, 'nome': 'luffy', 'Habilidades': ['Python', 'Ciencia de dados']}
]


# Retorna, altera e deleta um desenvolvedor por ID
@app.route('/dev/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = f'Desenvolvedor de {id} não existe'
            response = {'status': 'Erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Porcure o adiministrador da API'
            response = {'status': 'Erro', 'mensagem': mensagem}
        return jsonify(response)

    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'Status': 'Sucesso', 'Menssagem': 'Registro excluido'})


# Lista todos os desenvolvedores e permite registrar um novo desenvolvedor
@app.route('/dev/', methods=['GET', 'POST'])
def list_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    elif request.method == 'GET':
        return jsonify(desenvolvedores)


if __name__ == '__main__':
    app.run(debug=True)
