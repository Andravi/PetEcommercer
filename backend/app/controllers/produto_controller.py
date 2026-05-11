from app import db
from app.models.produto import Produto
from app.models.log_estoque import LogEstoque

class ProdutoController:
    
    @staticmethod
    def criar_produto(data, usuario_id):
        """Cria um novo produto"""
        produto = Produto(
            descricao=data['descricao'],
            preco=data['preco'],
            foto=data.get('foto'),
            quantidade=data['quantidade'],
            categoria_id=data['categoria_id']
        )
        
        db.session.add(produto)
        db.session.commit()
        
        # Criar log de estoque
        log = LogEstoque(
            produto_id=produto.id,
            usuario_id=usuario_id,
            quantidade_anterior=0,
            quantidade_nova=produto.quantidade,
            motivo='Produto criado'
        )
        db.session.add(log)
        db.session.commit()
        
        return produto.to_dict(), 201
    
    @staticmethod
    def listar_produtos(categoria_id=None):
        """Lista produtos, opcionalmente filtrado por categoria"""
        query = Produto.query
        if categoria_id:
            query = query.filter_by(categoria_id=categoria_id)
        
        produtos = query.all()
        return [p.to_dict() for p in produtos], 200
    
    @staticmethod
    def buscar_produto(id):
        """Busca um produto por ID"""
        produto = Produto.query.get(id)
        if not produto:
            return {'erro': 'Produto não encontrado'}, 404
        return produto.to_dict(), 200
    
    @staticmethod
    def atualizar_estoque(id, quantidade, usuario_id, motivo):
        """Atualiza o estoque de um produto com log"""
        produto = Produto.query.get(id)
        if not produto:
            return {'erro': 'Produto não encontrado'}, 404
        
        quantidade_anterior = produto.quantidade
        produto.quantidade = quantidade
        
        # Criar log
        log = LogEstoque(
            produto_id=produto.id,
            usuario_id=usuario_id,
            quantidade_anterior=quantidade_anterior,
            quantidade_nova=quantidade,
            motivo=motivo
        )
        
        db.session.add(log)
        db.session.commit()
        
        return produto.to_dict(), 200
    
    @staticmethod
    def deletar_produto(id):
        """Deleta um produto"""
        produto = Produto.query.get(id)
        if not produto:
            return {'erro': 'Produto não encontrado'}, 404
        
        db.session.delete(produto)
        db.session.commit()
        return {'mensagem': 'Produto deletado com sucesso'}, 200