from app import db

class Usuario(db.Model):
    __tablename__ = 'usuario'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    endereco = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    login = db.Column(db.String(50), unique=True, nullable=False)
    senha = db.Column(db.String(255), nullable=False)  # Armazenar hash
    administrador = db.Column(db.Boolean, nullable=False, default=False)
    
    # Relacionamentos
    vendas = db.relationship('Venda', backref='usuario', lazy=True)
    favoritos = db.relationship('UsuarioFavoritoProduto', backref='usuario', lazy=True, cascade='all, delete-orphan')
    carrinho_items = db.relationship('CarrinhoItem', backref='usuario', lazy=True, cascade='all, delete-orphan')
    logs_estoque = db.relationship('LogEstoque', backref='usuario', lazy=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'endereco': self.endereco,
            'email': self.email,
            'login': self.login,
            'administrador': self.administrador
        }