# app/routes/categoria_routes.py
from flask import Blueprint, request, jsonify
from app.controllers.categoria_controller import CategoriaController

categoria_bp = Blueprint('categoria', __name__)

@categoria_bp.route('/', methods=['GET'])
def listar():
    result, status = CategoriaController.listar_categorias()
    return jsonify(result), status

@categoria_bp.route('/', methods=['POST'])
def criar():
    data = request.get_json()
    result, status = CategoriaController.criar_categoria(data)
    return jsonify(result), status

@categoria_bp.route('/<int:id>', methods=['GET'])
def buscar(id):
    result, status = CategoriaController.buscar_categoria(id)
    return jsonify(result), status

@categoria_bp.route('/<int:id>', methods=['PUT'])
def atualizar(id):
    data = request.get_json()
    result, status = CategoriaController.atualizar_categoria(id, data)
    return jsonify(result), status

@categoria_bp.route('/<int:id>', methods=['DELETE'])
def deletar(id):
    result, status = CategoriaController.deletar_categoria(id)
    return jsonify(result), status