from app import db
from app.models.usuario import Usuario
from werkzeug.security import generate_password_hash, check_password_hash

class UsuarioController:
    
    @staticmethod
    def criar_usuario(data):
        """Cria um novo usuário"""
        # Verificar se login já existe
        if Usuario.query.filter_by(login=data['login']).first():
            return {'erro': 'Login já existe'}, 400
        
        usuario = Usuario(
            nome=data['nome'],
            endereco=data['endereco'],
            email=data['email'],
            login=data['login'],
            senha=generate_password_hash(data['senha']),
            administrador=data.get('administrador', False)
        )
        
        db.session.add(usuario)
        db.session.commit()
        
        return usuario.to_dict(), 201
    
    @staticmethod
    def listar_usuarios():
        """Lista todos os usuários"""
        usuarios = Usuario.query.all()
        return [u.to_dict() for u in usuarios], 200
    
    @staticmethod
    def buscar_usuario(id):
        """Busca um usuário por ID"""
        usuario = Usuario.query.get(id)
        if not usuario:
            return {'erro': 'Usuário não encontrado'}, 404
        return usuario.to_dict(), 200
    
    @staticmethod
    def atualizar_usuario(id, data):
        """Atualiza um usuário"""
        usuario = Usuario.query.get(id)
        if not usuario:
            return {'erro': 'Usuário não encontrado'}, 404
        
        # Atualizar campos
        if 'nome' in data:
            usuario.nome = data['nome']
        if 'endereco' in data:
            usuario.endereco = data['endereco']
        if 'email' in data:
            usuario.email = data['email']
        if 'senha' in data:
            usuario.senha = generate_password_hash(data['senha'])
        if 'administrador' in data:
            usuario.administrador = data['administrador']
        
        db.session.commit()
        return usuario.to_dict(), 200
    
    @staticmethod
    def deletar_usuario(id):
        """Deleta um usuário"""
        usuario = Usuario.query.get(id)
        if not usuario:
            return {'erro': 'Usuário não encontrado'}, 404
        
        db.session.delete(usuario)
        db.session.commit()
        return {'mensagem': 'Usuário deletado com sucesso'}, 200
    
    @staticmethod
    def autenticar(login, senha):
        """Autentica um usuário"""
        usuario = Usuario.query.filter_by(login=login).first()
        if usuario and check_password_hash(usuario.senha, senha):
            return usuario.to_dict(), 200
        return {'erro': 'Credenciais inválidas'}, 401