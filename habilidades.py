from flask_restful import Resource, request
import json

list_habilidades = {'habilidade': ['Pyton', 'Java', 'C#', 'PHP', 'Flask', 'Ruby', 'Unity', 'Blender', 'Mudbox']}


class Habilidades(Resource):
    def get(self):
        return list_habilidades

    def post(self):
        json_data = json.loads(request.data)
        lista = list_habilidades['habilidade'] # Seleciona lista
        resposta = json_data['habilidade'] # Selecionara resposta
        dados = lista + [resposta] # So aceita concatencação com lista
        list_habilidades['habilidade'] = dados
        return {'resposta': dados}


class Habilidades_id(Resource):
    # tratar erro
    def get(self, id):
        list = list_habilidades['habilidade']
        select_habilidades = list[id]
        return select_habilidades

    # tratar erro
    def put(self, id):
        dados = json.loads(request.data)
        list = list_habilidades['habilidade']
        list[id] = dados['habilidade']
        return list


    def delete(self, id):
        list = list_habilidades['habilidade']
        list.pop(id)
        return list

