from app import db

class Produto(db.Model):
    __tablename__ = 'produto'
    
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(200), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    foto = db.Column(db.String(500), nullable=True)
    quantidade = db.Column(db.Integer, nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'), nullable=False)
    
    # Relacionamentos
    vendas = db.relationship('VendaProduto', backref='produto', lazy=True)
    favoritos = db.relationship('UsuarioFavoritoProduto', backref='produto', lazy=True, cascade='all, delete-orphan')
    carrinho_items = db.relationship('CarrinhoItem', backref='produto', lazy=True, cascade='all, delete-orphan')
    logs_estoque = db.relationship('LogEstoque', backref='produto', lazy=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'descricao': self.descricao,
            'preco': self.preco,
            'foto': self.foto,
            'quantidade': self.quantidade,
            'categoria_id': self.categoria_id,
            'categoria_descricao': self.categoria.descricao if self.categoria else None
        }