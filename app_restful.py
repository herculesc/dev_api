from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import Habilidades, Habilidades_id
import json

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {'id': 0, 'nome': 'Hercules', 'Habilidades': ['Python', 'Machine Learning', 'Flask', 'Rest API', 'Ciencia de dados']},
    {'id': 1, 'nome': 'kira', 'Habilidades': ['Python', 'Flask', 'Rest API']},
    {'id': 2, 'nome': 'luffy', 'Habilidades': ['Python', 'Ciencia de dados']}
]

# Retorna, altera e deleta um desenvolvedor por ID
class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = f'Desenvolvedor de {id} não existe'
            response = {'status': 'Erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Porcure o adiministrador da API'
            response = {'status': 'Erro', 'mensagem': mensagem}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        try:
            desenvolvedores.pop(id)
            mensagem = 'Registro excluido'
            response = {'Status': 'Sucesso', 'Menssagem': mensagem}

        except IndexError:
            mensagem = 'Não é possivel excluir um desenvolvedor que não existe'
            response = {'Status': 'Erro', 'Menssagem': mensagem}

        except Exception:
            mensagem = 'Erro não foi possivel excluir. Porcure o adiministrador da API'
            response = {'status': 'Erro', 'mensagem': mensagem}

        return response


# Lista todos os desenvolvedores e permite registrar um novo desenvolvedor
class list_desenvolvedores(Resource):
    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]

    def get(self):
        return desenvolvedores


api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(list_desenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidades/')
api.add_resource(Habilidades_id, '/habilidades/<int:id>/')

if __name__ == '__main__':
    app.run(debug=True)
