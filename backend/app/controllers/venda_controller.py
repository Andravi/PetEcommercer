from app import db
from app.models.venda import Venda
from app.models.venda_produto import VendaProduto
from app.models.carrinho_item import CarrinhoItem
from app.controllers.produto_controller import ProdutoController
from datetime import datetime

class VendaController:
    
    @staticmethod
    def criar_venda(usuario_id):
        """Cria uma venda a partir dos itens do carrinho"""
        # Todo Trocar lógica
        carrinho_items = CarrinhoItem.query.filter_by(usuario_id=usuario_id).all()
        
        if not carrinho_items:
            return {'erro': 'Carrinho vazio'}, 400
        
        # Criar venda
        venda = Venda(
            usuario_id=usuario_id,
            data_hora=datetime.now()
        )
        db.session.add(venda)
        db.session.flush()  # Para obter o ID da venda
        
        # Processar cada item do carrinho
        for item in carrinho_items:
            # Verificar estoque novamente
            if item.produto.quantidade < item.quantidade:
                db.session.rollback()
                return {'erro': f'Estoque insuficiente para {item.produto.descricao}'}, 400
            
            # Adicionar item à venda
            venda_produto = VendaProduto(
                venda_id=venda.id,
                produto_id=item.produto_id,
                preco=item.produto.preco,
                quantidade=item.quantidade
            )
            db.session.add(venda_produto)
            
            # Atualizar estoque
            nova_quantidade = item.produto.quantidade - item.quantidade
            from app.controllers.produto_controller import ProdutoController
            ProdutoController.atualizar_estoque(
                item.produto_id, 
                nova_quantidade, 
                usuario_id, 
                f'Venda #{venda.id} - Compra realizada'
            )
        
        # Limpar carrinho
        CarrinhoItem.query.filter_by(usuario_id=usuario_id).delete()
        
        db.session.commit()
        
        return venda.to_dict(), 201
    
    @staticmethod
    def listar_vendas():
        """Lista todas as vendas"""
        vendas = Venda.query.all()
        return [v.to_dict() for v in vendas], 200
    
    @staticmethod
    def listar_vendas_por_usuario(usuario_id):
        """Lista vendas de um usuário específico"""
        vendas = Venda.query.filter_by(usuario_id=usuario_id).all()
        return [v.to_dict() for v in vendas], 200
    
    @staticmethod
    def buscar_venda(id):
        """Busca uma venda por ID"""
        venda = Venda.query.get(id)
        if not venda:
            return {'erro': 'Venda não encontrada'}, 404
        return venda.to_dict(), 200
    
    @staticmethod
    def cancelar_venda(id, usuario_id, motivo):
        """Cancela uma venda e restaura o estoque"""
        venda = Venda.query.get(id)
        if not venda:
            return {'erro': 'Venda não encontrada'}, 404
        
        # Restaurar estoque para cada produto da venda
        for item in venda.produtos:
            produto = item.produto
            nova_quantidade = produto.quantidade + item.quantidade
            
            from app.controllers.produto_controller import ProdutoController
            ProdutoController.atualizar_estoque(
                item.produto_id,
                nova_quantidade,
                usuario_id,
                f'Cancelamento da venda #{id} - {motivo}'
            )
        
        # Deletar a venda (ou marcar como cancelada se tiver campo status)
        db.session.delete(venda)
        db.session.commit()
        
        return {'mensagem': f'Venda #{id} cancelada com sucesso'}, 200