from app import db
from datetime import datetime

class LogEstoque(db.Model):
    __tablename__ = 'log_estoque'
    
    id = db.Column(db.Integer, primary_key=True)
    produto_id = db.Column(db.Integer, db.ForeignKey('produto.id'), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    quantidade_anterior = db.Column(db.Integer, nullable=False)
    quantidade_nova = db.Column(db.Integer, nullable=False)
    data_alteracao = db.Column(db.DateTime, nullable=False, default=datetime.now)
    motivo = db.Column(db.String(200), nullable=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            'produto_id': self.produto_id,
            'produto_descricao': self.produto.descricao if self.produto else None,
            'usuario_id': self.usuario_id,
            'usuario_nome': self.usuario.nome if self.usuario else None,
            'quantidade_anterior': self.quantidade_anterior,
            'quantidade_nova': self.quantidade_nova,
            'data_alteracao': self.data_alteracao.isoformat(),
            'motivo': self.motivo
        }