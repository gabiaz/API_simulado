# 
# simular API = Lugar para disponibilizar recursos e funcionalidades.

from flask import Flask, jsonify, request
app=Flask(__name__)

grupo = [
    {
        "id": 0,
        "name": "Pedro",
        "idade": "10"
    },
    {
        "id": 1,
        "name": "Tiago",
        "idade": "20"
    },
    {
        "id": 2,
        "name": "Joao",
        "idade": "30"
    }
]

#.
# 01 - Consultar dados de todo o grupo:
@api.route('/grupo',methods=["GET"])

def tudo():

    return jsonify(grupo)

# 02 - Consultar dados por id:
@api.route("/grupo/<int:id>", methods=["GET"])
def dados_da_pessoa(id):
    
    for pessoa in grupo:
        if pessoa.get("id") == id:
            
            return jsonify(pessoa)
        
# 03 - Editar itens:
@api.route("/grupo/<int:id>", methods=["PUT"])

def editar_por_id(id):
    
    editado= request.get_json()
    for key,valor in enumerate(grupo):
        if valor.get("id")==id:
            grupo[key].update(editado)
            
            return jsonify(grupo[key])
        
# 04 - Criar/Adicionar
@api.route("/grupo/", methods=["POST"])

def novo():
    nova_pessoa = request.get_json()
    grupo.append(nova_pessoa)

    return jsonify(grupo)

# 05 - Excluir
@api.route("/grupo/<int:id>", methods=["DELETE"])

def excluir(id):
    for key,value in enumerate(grupo):
        if value.get("id")==id:
            del grupo[key]

    return jsonify(grupo)

api.run(port=5000,host="localhost",debug=True)