from app import db
from app.models.categoria import Categoria

class CategoriaController:
    
    @staticmethod
    def criar_categoria(data):
        """Cria uma nova categoria"""
        categoria = Categoria(descricao=data['descricao'])
        db.session.add(categoria)
        db.session.commit()
        return categoria.to_dict(), 201
    
    @staticmethod
    def listar_categorias():
        """Lista todas as categorias"""
        categorias = Categoria.query.all()
        return [c.to_dict() for c in categorias], 200
    
    @staticmethod
    def buscar_categoria(id):
        """Busca uma categoria por ID"""
        categoria = Categoria.query.get(id)
        if not categoria:
            return {'erro': 'Categoria não encontrada'}, 404
        return categoria.to_dict(), 200
    
    @staticmethod
    def atualizar_categoria(id, data):
        """Atualiza uma categoria"""
        categoria = Categoria.query.get(id)
        if not categoria:
            return {'erro': 'Categoria não encontrada'}, 404
        
        if 'descricao' in data:
            categoria.descricao = data['descricao']
        
        db.session.commit()
        return categoria.to_dict(), 200
    
    @staticmethod
    def deletar_categoria(id):
        """Deleta uma categoria (se não tiver produtos associados)"""
        categoria = Categoria.query.get(id)
        if not categoria:
            return {'erro': 'Categoria não encontrada'}, 404
        
        # Verificar se existem produtos nesta categoria
        if categoria.produtos:
            return {'erro': 'Não é possível deletar categoria com produtos associados'}, 400
        
        db.session.delete(categoria)
        db.session.commit()
        return {'mensagem': 'Categoria deletada com sucesso'}, 200