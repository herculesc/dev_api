from flask_restful import Resource

list_habilidades = ['Pyton', 'Java', 'C#', 'PHP', 'Flask', 'Ruby','Unity', 'Blender', 'mudbox' ]


class Habilidades(Resource):
    def get(self):
        return list_habilidades

