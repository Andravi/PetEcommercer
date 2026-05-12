from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    from app.routes import (
        usuario_bp, categoria_bp, produto_bp, 
        venda_bp, carrinho_bp, favorito_bp,
        log_estoque_bp  
    )
    
    app.register_blueprint(usuario_bp, url_prefix='/api/usuarios')
    app.register_blueprint(categoria_bp, url_prefix='/api/categorias')
    app.register_blueprint(produto_bp, url_prefix='/api/produtos')
    app.register_blueprint(venda_bp, url_prefix='/api/vendas')
    app.register_blueprint(carrinho_bp, url_prefix='/api/carrinho')
    app.register_blueprint(favorito_bp, url_prefix='/api/favoritos')  
    app.register_blueprint(log_estoque_bp, url_prefix='/api/logs/estoque')  
    
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'erro': 'Recurso não encontrado'}), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        db.session.rollback()
        return jsonify({'erro': 'Erro interno do servidor'}), 500
    
    return app