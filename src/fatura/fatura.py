from flask import Blueprint, jsonify,request
import sys
from db import db_mongo_class
from datetime import datetime
from bson.json_util import dumps, loads

fatura_bp = Blueprint('fatura', __name__)



def check(list):
    check = all(i == list[0] for i in list)
    if check:
        return list[0],check
    return 'Erro', check 



# Rota para criar uma nova fatura
@fatura_bp.route('/fatura/cria_fatura', methods=['POST'])
def create_fatura():
    try:
        data = request.json
        db_objt = db_mongo_class()
        collection = db_objt.get_collection()
        maior_id = list(collection.find().sort('id_fatura', -1).limit(1))[0]['id_fatura']
        print(maior_id,file=sys.stderr)

        next_id = maior_id + 1
        
        current_datetime = datetime.now()
        
        fatura = {"id_fatura":next_id, "id_pedido":data['id_pedido'], "id_cliente":data.get('id_cliente'), "valor":data.get('valor'), "status":data.get('status'), "data_fatura":current_datetime}
        collection.insert_one(fatura)
        return jsonify({"message": "Fatura criado com sucesso"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400




# Rota para recuperar a fatura
@fatura_bp.route('/fatura/consulta_fatura/<int:id>', methods=['GET'])
def get_fatura(id):
    try:
        db_objt = db_mongo_class()
        collection = db_objt.get_collection()
        fatura = collection.find_one({"id_fatura": id})
        if fatura:
            return dumps(fatura), 200
        else:
            return jsonify({"message": "fatura não encontrada"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400



# Rota para atualizar um fatura pelo ID
@fatura_bp.route('/fatura/atualiza_fatura/<int:id>', methods=['PUT'])
def update_fatura_status(id):
    try:
        data = request.json
        db_objt = db_mongo_class()
        collection = db_objt.get_collection()
        collection.update_one({"id_fatura": id}, {"$set": {"status": data.get('status')}})
        return jsonify({"message": "Fatura atualizada com sucesso"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400



@fatura_bp.route('/fatura/atualiza_fatura_pago/<int:id>', methods=['PUT'])
def update_fatura_status_pago(id):
    try:
        db_objt = db_mongo_class()
        collection = db_objt.get_collection()
        collection.update_one({"id_fatura": id}, {"$set": {"status": 2}})

        return jsonify({"message": "Fatura atualizada com sucesso"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400



@fatura_bp.route('/fatura/atualiza_fatura_nao_pago/<int:id>', methods=['PUT'])
def update_fatura_status_nao_pago(id):
    try:
        db_objt = db_mongo_class()
        collection = db_objt.get_collection()
        collection.update_one({"id_fatura": id}, {"$set": {"status": 1}})

        return jsonify({"message": "Fatura atualizada com sucesso"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@fatura_bp.route('/fatura/atualiza_fatura_cancelado/<int:id>', methods=['PUT'])
def update_fatura_status_cancelado(id):
    try:
        db_objt = db_mongo_class()
        collection = db_objt.get_collection()
        collection.update_one({"id_fatura": id}, {"$set": {"status": 3}})

        return jsonify({"message": "Fatura cancelada com sucesso"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400




# Rota para recuperar todx consulta_all_fatura
@fatura_bp.route('/fatura/consulta_all/', methods=['GET'])
def consulta_all_fatura():
    try:
        db_objt = db_mongo_class()
        collection = db_objt.get_collection()
        faturas = list(collection.find())
        return dumps(faturas),200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


