from sqlalchemy import create_engine, Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

db = create_engine("sqlite:///meubanco.db")
Session = sessionmaker(bind=db)
session = Session()


Base = declarative_base()

#as tabelas
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)
    ativo = Column("ativo", Boolean)

    def __init__(self, nome, email, senha, ativo=True):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo


# Livros
class Livro(Base):
    __tablename__ = "livros"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    titulo = Column("titulo", String)
    qtde_paginas = Column("qtde_paginas", Integer)
    dono = Column("dono", ForeignKey("usuarios.id"))

    def __init__(self, titulo, qtde_paginas, dono):
        self.titulo = titulo
        self.qtde_paginas = qtde_paginas
        self.dono = dono


Base.metadata.create_all(bind=db)
'''
CRUD

C - Create
usuario = Usuario(nome="matheus", email="qlqcoisa777@gmail.com", senha="123123")
session.add(usuario) --> adiciona
session.commit() --> commit ou seja salva o item no banco de dados

R - READ
lista_usuarios = session.query(Usuario).all() --> (.all seleciona todos)
usuario2 = session.query(Usuario).filter_by(email="qlqcoisa666@gmail.com").first() --> query permite fazer uma consulta, o filtro é literalmente um filtro
print(usuario2) --> (lista python)
print(usuario2.nome) 
print(usuario2.email) 

livro = Livro(titulo="Nome do Vento", qtde_paginas=1000, dono=usuario2.id)
session.add(livro) --> adiciona
session.commit() --> commit ou seja salva o item no banco de dados

U - Update
usuario2.nome = "Matheus kenzo" --> atualiza
session.add(usuario2) --> adiciona o usuario dnv
session.commit() --> salva

D - Delete
session.delete(usuario2) --> literal deleta
session.commit()

qualquer edição feita sempre dê commits para salvar sempre as info.
'''
#existe um aplicativo chamado db browser que da para visualizar melhor o banco de dados