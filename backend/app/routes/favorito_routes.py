# app/routes/favorito_routes.py
from flask import Blueprint, request, jsonify
from app.controllers.favorito_controller import FavoritoController

favorito_bp = Blueprint('favorito', __name__)

@favorito_bp.route('/<int:usuario_id>', methods=['GET'])
def listar_favoritos(usuario_id):
    """GET /api/favoritos/{usuario_id} - Lista favoritos do usuário"""
    result, status = FavoritoController.listar_favoritos(usuario_id)
    return jsonify(result), status

@favorito_bp.route('/<int:usuario_id>/<int:produto_id>', methods=['POST'])
def adicionar_favorito(usuario_id, produto_id):
    """POST /api/favoritos/{usuario_id}/{produto_id} - Adiciona aos favoritos"""
    result, status = FavoritoController.adicionar_favorito(usuario_id, produto_id)
    return jsonify(result), status

@favorito_bp.route('/<int:usuario_id>/<int:produto_id>', methods=['DELETE'])
def remover_favorito(usuario_id, produto_id):
    """DELETE /api/favoritos/{usuario_id}/{produto_id} - Remove dos favoritos"""
    result, status = FavoritoController.remover_favorito(usuario_id, produto_id)
    return jsonify(result), status

@favorito_bp.route('/<int:usuario_id>/verificar/<int:produto_id>', methods=['GET'])
def verificar_favorito(usuario_id, produto_id):
    """GET /api/favoritos/{usuario_id}/verificar/{produto_id} - Verifica se é favorito"""
    result, status = FavoritoController.verificar_favorito(usuario_id, produto_id)
    return jsonify(result), status