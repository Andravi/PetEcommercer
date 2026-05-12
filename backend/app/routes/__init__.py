from app.routes.usuario_routes import usuario_bp
from app.routes.categoria_routes import categoria_bp
from app.routes.produto_routes import produto_bp
from app.routes.venda_routes import venda_bp
from app.routes.carrinho_routes import carrinho_bp
from app.routes.favorito_routes import favorito_bp  
from app.routes.log_estoque_routes import log_estoque_bp  

__all__ = [
    'usuario_bp',
    'categoria_bp',
    'produto_bp',
    'venda_bp',
    'carrinho_bp',
    'favorito_bp',
    'log_estoque_bp'
]