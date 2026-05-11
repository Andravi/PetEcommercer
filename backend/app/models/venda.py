from app import db
from datetime import datetime

class Venda(db.Model):
    __tablename__ = 'venda'
    
    id = db.Column(db.Integer, primary_key=True)
    data_hora = db.Column(db.DateTime, nullable=False, default=datetime.now)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    
    # Relacionamento
    produtos = db.relationship('VendaProduto', backref='venda', lazy=True, cascade='all, delete-orphan')
    
    def to_dict(self):
        return {
            'id': self.id,
            'data_hora': self.data_hora.isoformat(),
            'usuario_id': self.usuario_id,
            'usuario_nome': self.usuario.nome if self.usuario else None,
            'total': sum(item.preco * item.quantidade for item in self.produtos),
            'produtos': [item.to_dict() for item in self.produtos]
        }