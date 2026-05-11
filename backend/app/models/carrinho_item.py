from app import db
from datetime import datetime

class CarrinhoItem(db.Model):
    __tablename__ = 'carrinho_item'
    
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    produto_id = db.Column(db.Integer, db.ForeignKey('produto.id'), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    data_adicao = db.Column(db.DateTime, nullable=False, default=datetime.now)
    
    __table_args__ = (db.UniqueConstraint('usuario_id', 'produto_id', name='unique_usuario_produto_carrinho'),)
    
    def to_dict(self):
        return {
            'id': self.id,
            'usuario_id': self.usuario_id,
            'produto_id': self.produto_id,
            'produto_descricao': self.produto.descricao if self.produto else None,
            'preco': self.produto.preco if self.produto else None,
            'quantidade': self.quantidade,
            'data_adicao': self.data_adicao.isoformat(),
            'subtotal': (self.produto.preco * self.quantidade) if self.produto else 0
        }