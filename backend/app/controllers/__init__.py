# app/controllers/__init__.py
"""
Exporta todos os controllers para facilitar importações
"""

from app.controllers.usuario_controller import UsuarioController
from app.controllers.categoria_controller import CategoriaController
from app.controllers.produto_controller import ProdutoController
from app.controllers.venda_controller import VendaController
from app.controllers.carrinho_controller import CarrinhoController
from app.controllers.favorito_controller import FavoritoController
from app.controllers.log_estoque_controller import LogEstoqueController

__all__ = [
    'UsuarioController',
    'CategoriaController',
    'ProdutoController',
    'VendaController',
    'CarrinhoController',
    'FavoritoController',
    'LogEstoqueController'
]