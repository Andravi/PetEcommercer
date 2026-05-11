# app/routes/venda_routes.py
from flask import Blueprint, request, jsonify
from app.controllers.venda_controller import VendaController

venda_bp = Blueprint('venda', __name__)

@venda_bp.route('/', methods=['GET'])
def listar():
    """GET /api/vendas/ - Lista todas as vendas"""
    result, status = VendaController.listar_vendas()
    return jsonify(result), status

@venda_bp.route('/usuario/<int:usuario_id>', methods=['GET'])
def listar_por_usuario(usuario_id):
    """GET /api/vendas/usuario/{usuario_id} - Lista vendas do usuário"""
    result, status = VendaController.listar_vendas_por_usuario(usuario_id)
    return jsonify(result), status

@venda_bp.route('/', methods=['POST'])
def criar():
    """POST /api/vendas/ - Cria nova venda (finaliza compra)"""
    data = request.get_json()
    result, status = VendaController.criar_venda(data['usuario_id'])
    return jsonify(result), status

@venda_bp.route('/<int:id>', methods=['GET'])
def buscar(id):
    """GET /api/vendas/{id} - Busca venda por ID"""
    result, status = VendaController.buscar_venda(id)
    return jsonify(result), status