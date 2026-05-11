from flask import Blueprint, request, jsonify
from app.controllers.carrinho_controller import CarrinhoController

carrinho_bp = Blueprint('carrinho', __name__)

@carrinho_bp.route('/<int:usuario_id>', methods=['GET'])
def listar_carrinho(usuario_id):
    """GET /api/carrinho/{usuario_id} - Lista carrinho do usuário"""
    result, status = CarrinhoController.listar_carrinho(usuario_id)
    return jsonify(result), status

@carrinho_bp.route('/<int:usuario_id>/adicionar', methods=['POST'])
def adicionar(usuario_id):
    """POST /api/carrinho/{usuario_id}/adicionar - Adiciona item ao carrinho"""
    data = request.get_json()
    result, status = CarrinhoController.adicionar_ao_carrinho(
        usuario_id, 
        data['produto_id'], 
        data['quantidade']
    )
    return jsonify(result), status

@carrinho_bp.route('/<int:usuario_id>/atualizar', methods=['PUT'])
def atualizar(usuario_id):
    """PUT /api/carrinho/{usuario_id}/atualizar - Atualiza quantidade"""
    data = request.get_json()
    result, status = CarrinhoController.atualizar_quantidade(
        usuario_id, 
        data['produto_id'], 
        data['quantidade']
    )
    return jsonify(result), status

@carrinho_bp.route('/<int:usuario_id>/limpar', methods=['DELETE'])
def limpar(usuario_id):
    """DELETE /api/carrinho/{usuario_id}/limpar - Limpa carrinho"""
    result, status = CarrinhoController.limpar_carrinho(usuario_id)
    return jsonify(result), status