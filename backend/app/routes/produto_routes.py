from flask import Blueprint, request, jsonify
from app.controllers.produto_controller import ProdutoController

produto_bp = Blueprint('produto', __name__)

@produto_bp.route('/', methods=['GET'])
def listar():
    """GET /api/produtos/ - Lista produtos (opcional: ?categoria_id=1)"""
    categoria_id = request.args.get('categoria_id', type=int)
    result, status = ProdutoController.listar_produtos(categoria_id)
    return jsonify(result), status

@produto_bp.route('/', methods=['POST'])
def criar():
    """POST /api/produtos/ - Cria novo produto"""
    data = request.get_json()
    usuario_id = request.headers.get('X-Usuario-ID', 1)  # Idealmente viria do token JWT
    result, status = ProdutoController.criar_produto(data, usuario_id)
    return jsonify(result), status

@produto_bp.route('/<int:id>', methods=['GET'])
def buscar(id):
    """GET /api/produtos/{id} - Busca produto por ID"""
    result, status = ProdutoController.buscar_produto(id)
    return jsonify(result), status

@produto_bp.route('/<int:id>/estoque', methods=['PUT'])
def atualizar_estoque(id):
    """PUT /api/produtos/{id}/estoque - Atualiza estoque"""
    data = request.get_json()
    usuario_id = request.headers.get('X-Usuario-ID', 1)
    result, status = ProdutoController.atualizar_estoque(
        id, 
        data['quantidade'], 
        usuario_id, 
        data.get('motivo', 'Atualização manual')
    )
    return jsonify(result), status

@produto_bp.route('/<int:id>', methods=['DELETE'])
def deletar(id):
    """DELETE /api/produtos/{id} - Deleta produto"""
    result, status = ProdutoController.deletar_produto(id)
    return jsonify(result), status