# app/controllers/carrinho_controller.py
from app import db
from app.models.carrinho_item import CarrinhoItem
from app.models.produto import Produto

class CarrinhoController:
    
    @staticmethod
    def adicionar_ao_carrinho(usuario_id, produto_id, quantidade):
        """Adiciona item ao carrinho"""
        # Verificar se produto existe e tem estoque
        produto = Produto.query.get(produto_id)
        if not produto:
            return {'erro': 'Produto não encontrado'}, 404
        
        if produto.quantidade < quantidade:
            return {'erro': 'Estoque insuficiente'}, 400
        
        # Verificar se já existe no carrinho
        item = CarrinhoItem.query.filter_by(usuario_id=usuario_id, produto_id=produto_id).first()
        
        if item:
            item.quantidade += quantidade
        else:
            item = CarrinhoItem(
                usuario_id=usuario_id,
                produto_id=produto_id,
                quantidade=quantidade
            )
            db.session.add(item)
        
        db.session.commit()
        return item.to_dict(), 200
    
    @staticmethod
    def listar_carrinho(usuario_id):
        """Lista itens do carrinho do usuário"""
        items = CarrinhoItem.query.filter_by(usuario_id=usuario_id).all()
        total = sum(item.produto.preco * item.quantidade for item in items)
        
        return {
            'itens': [item.to_dict() for item in items],
            'total': total
        }, 200
    
    @staticmethod
    def atualizar_quantidade(usuario_id, produto_id, quantidade):
        """Atualiza quantidade de item no carrinho"""
        item = CarrinhoItem.query.filter_by(usuario_id=usuario_id, produto_id=produto_id).first()
        if not item:
            return {'erro': 'Item não encontrado no carrinho'}, 404
        
        if quantidade <= 0:
            db.session.delete(item)
        else:
            # Verificar estoque
            if item.produto.quantidade < quantidade:
                return {'erro': 'Estoque insuficiente'}, 400
            item.quantidade = quantidade
        
        db.session.commit()
        return {'mensagem': 'Carrinho atualizado'}, 200
    
    @staticmethod
    def limpar_carrinho(usuario_id):
        """Remove todos os itens do carrinho"""
        CarrinhoItem.query.filter_by(usuario_id=usuario_id).delete()
        db.session.commit()
        return {'mensagem': 'Carrinho limpo com sucesso'}, 200
