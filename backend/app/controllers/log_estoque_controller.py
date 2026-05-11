from app import db
from app.models.log_estoque import LogEstoque

class LogEstoqueController:
    
    @staticmethod
    def listar_logs(produto_id=None, usuario_id=None):
        """Lista logs de estoque com filtros opcionais"""
        query = LogEstoque.query
        
        if produto_id:
            query = query.filter_by(produto_id=produto_id)
        
        if usuario_id:
            query = query.filter_by(usuario_id=usuario_id)
        
        logs = query.order_by(LogEstoque.data_alteracao.desc()).all()
        return [log.to_dict() for log in logs], 200
    
    @staticmethod
    def buscar_log(id):
        """Busca um log específico por ID"""
        log = LogEstoque.query.get(id)
        if not log:
            return {'erro': 'Log não encontrado'}, 404
        return log.to_dict(), 200
    
    @staticmethod
    def listar_por_periodo(data_inicio, data_fim):
        """Lista logs em um período específico"""
        logs = LogEstoque.query.filter(
            LogEstoque.data_alteracao.between(data_inicio, data_fim)
        ).order_by(LogEstoque.data_alteracao.desc()).all()
        
        return [log.to_dict() for log in logs], 200
    
    @staticmethod
    def relatorio_alteracoes_produto(produto_id, limite=50):
        """Relatório de alterações de estoque de um produto específico"""
        logs = LogEstoque.query.filter_by(produto_id=produto_id)\
            .order_by(LogEstoque.data_alteracao.desc())\
            .limit(limite)\
            .all()
        
        if not logs:
            return {'mensagem': 'Nenhuma alteração encontrada para este produto'}, 404
        
        return {
            'produto_id': produto_id,
            'produto_descricao': logs[0].produto.descricao if logs else None,
            'total_alteracoes': len(logs),
            'alteracoes': [log.to_dict() for log in logs]
        }, 200