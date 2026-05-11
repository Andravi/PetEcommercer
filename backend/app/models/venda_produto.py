from app import db

class VendaProduto(db.Model):
    __tablename__ = 'venda_produto'
    
    venda_id = db.Column(db.Integer, db.ForeignKey('venda.id'), primary_key=True)
    produto_id = db.Column(db.Integer, db.ForeignKey('produto.id'), primary_key=True)
    preco = db.Column(db.Float, nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    
    def to_dict(self):
        return {
            'venda_id': self.venda_id,
            'produto_id': self.produto_id,
            'produto_descricao': self.produto.descricao if self.produto else None,
            'preco': self.preco,
            'quantidade': self.quantidade,
            'subtotal': self.preco * self.quantidade
        }