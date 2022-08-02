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
        try:
            list = list_habilidades['habilidade']
            select_habilidades = list[id]
            mensagem = f'Habilidade {select_habilidades} encontrada'
            response = {'status': 'Sucesso', 'mensagem': mensagem}

        except IndexError:
            mensagem = f'Habilidade não existe'
            response = {'status': 'Erro', 'mensagem': mensagem}

        except Exception:
            mensagem = 'Erro não foi possivel excluir. Porcure o adiministrador da API'
            response = {'status': 'Erro', 'mensagem': mensagem}

        return response

    # tratar erro
    def put(self, id):
        dados = json.loads(request.data)
        list = list_habilidades['habilidade']
        old_habilidade = list[id]
        list[id] = dados['habilidade']
        mensagem = f'Habilidade {old_habilidade} foi atualizada para {list[id]}'
        response = {'status': 'Sucesso', 'mensagem': mensagem}
        return response

    def delete(self, id):
        list = list_habilidades['habilidade']
        list.pop(id)
        return list
