from flask import Blueprint, request, jsonify
from app.controllers.usuario_controller import UsuarioController

usuario_bp = Blueprint('usuario', __name__)

@usuario_bp.route('/', methods=['GET'])
def listar():
    """GET /api/usuarios/ - Lista todos os usuários"""
    result, status = UsuarioController.listar_usuarios()
    return jsonify(result), status

@usuario_bp.route('/', methods=['POST'])
def criar():
    """POST /api/usuarios/ - Cria novo usuário"""
    data = request.get_json()
    result, status = UsuarioController.criar_usuario(data)
    return jsonify(result), status

@usuario_bp.route('/<int:id>', methods=['GET'])
def buscar(id):
    """GET /api/usuarios/{id} - Busca usuário por ID"""
    result, status = UsuarioController.buscar_usuario(id)
    return jsonify(result), status

@usuario_bp.route('/<int:id>', methods=['PUT'])
def atualizar(id):
    """PUT /api/usuarios/{id} - Atualiza usuário"""
    data = request.get_json()
    result, status = UsuarioController.atualizar_usuario(id, data)
    return jsonify(result), status

@usuario_bp.route('/<int:id>', methods=['DELETE'])
def deletar(id):
    """DELETE /api/usuarios/{id} - Deleta usuário"""
    result, status = UsuarioController.deletar_usuario(id)
    return jsonify(result), status

@usuario_bp.route('/auth', methods=['POST'])
def autenticar():
    """POST /api/usuarios/auth - Autentica usuário"""
    data = request.get_json()
    result, status = UsuarioController.autenticar(data.get('login'), data.get('senha'))
    return jsonify(result), status