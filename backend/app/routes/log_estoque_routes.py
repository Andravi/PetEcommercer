# app/routes/log_estoque_routes.py
from flask import Blueprint, request, jsonify
from app.controllers.log_estoque_controller import LogEstoqueController
from datetime import datetime

log_estoque_bp = Blueprint('log_estoque', __name__)

@log_estoque_bp.route('/', methods=['GET'])
def listar_logs():
    """GET /api/logs/estoque?produto_id=1&usuario_id=2 - Lista logs com filtros"""
    produto_id = request.args.get('produto_id', type=int)
    usuario_id = request.args.get('usuario_id', type=int)
    
    result, status = LogEstoqueController.listar_logs(produto_id, usuario_id)
    return jsonify(result), status

@log_estoque_bp.route('/<int:id>', methods=['GET'])
def buscar_log(id):
    """GET /api/logs/estoque/{id} - Busca log por ID"""
    result, status = LogEstoqueController.buscar_log(id)
    return jsonify(result), status

@log_estoque_bp.route('/periodo', methods=['GET'])
def listar_por_periodo():
    """GET /api/logs/estoque/periodo?inicio=2024-01-01&fim=2024-12-31"""
    data_inicio = datetime.fromisoformat(request.args.get('inicio'))
    data_fim = datetime.fromisoformat(request.args.get('fim'))
    
    result, status = LogEstoqueController.listar_por_periodo(data_inicio, data_fim)
    return jsonify(result), status

@log_estoque_bp.route('/produto/<int:produto_id>/relatorio', methods=['GET'])
def relatorio_produto(produto_id):
    """GET /api/logs/estoque/produto/{produto_id}/relatorio?limite=50"""
    limite = request.args.get('limite', 50, type=int)
    result, status = LogEstoqueController.relatorio_alteracoes_produto(produto_id, limite)
    return jsonify(result), status