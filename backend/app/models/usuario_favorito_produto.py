from app import db
from datetime import datetime

class UsuarioFavoritoProduto(db.Model):
    __tablename__ = 'usuario_favorito_produto'
    
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), primary_key=True)
    produto_id = db.Column(db.Integer, db.ForeignKey('produto.id'), primary_key=True)
    data_favorito = db.Column(db.DateTime, nullable=False, default=datetime.now)
    
    def to_dict(self):
        return {
            'usuario_id': self.usuario_id,
            'produto_id': self.produto_id,
            'produto_descricao': self.produto.descricao if self.produto else None,
            'data_favorito': self.data_favorito.isoformat()
        }