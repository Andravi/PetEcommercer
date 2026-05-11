# app/controllers/favorito_controller.py
from app import db
from app.models.usuario_favorito_produto import UsuarioFavoritoProduto
from datetime import datetime

class FavoritoController:
    
    @staticmethod
    def adicionar_favorito(usuario_id, produto_id):
        """Adiciona um produto aos favoritos do usuário"""
        # Verificar se já está nos favoritos
        existe = UsuarioFavoritoProduto.query.filter_by(
            usuario_id=usuario_id, 
            produto_id=produto_id
        ).first()
        
        if existe:
            return {'erro': 'Produto já está nos favoritos'}, 400
        
        favorito = UsuarioFavoritoProduto(
            usuario_id=usuario_id,
            produto_id=produto_id,
            data_favorito=datetime.now()
        )
        
        db.session.add(favorito)
        db.session.commit()
        
        return favorito.to_dict(), 201
    
    @staticmethod
    def remover_favorito(usuario_id, produto_id):
        """Remove um produto dos favoritos"""
        favorito = UsuarioFavoritoProduto.query.filter_by(
            usuario_id=usuario_id, 
            produto_id=produto_id
        ).first()
        
        if not favorito:
            return {'erro': 'Produto não está nos favoritos'}, 404
        
        db.session.delete(favorito)
        db.session.commit()
        
        return {'mensagem': 'Produto removido dos favoritos'}, 200
    
    @staticmethod
    def listar_favoritos(usuario_id):
        """Lista todos os favoritos de um usuário"""
        favoritos = UsuarioFavoritoProduto.query.filter_by(usuario_id=usuario_id).all()
        return [f.to_dict() for f in favoritos], 200
    
    @staticmethod
    def verificar_favorito(usuario_id, produto_id):
        """Verifica se um produto está nos favoritos do usuário"""
        favorito = UsuarioFavoritoProduto.query.filter_by(
            usuario_id=usuario_id, 
            produto_id=produto_id
        ).first()
        
        return {'favorito': favorito is not None}, 200