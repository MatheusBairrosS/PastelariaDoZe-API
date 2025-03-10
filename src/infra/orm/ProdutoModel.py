from sqlalchemy import Column, VARCHAR, Integer, Boolean
import db

# ORM
class ProdutoDB(db.Base):
    __tablename__ = 'tb_produto'
    
    id_produto = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nome = Column(VARCHAR(100), nullable=False)
    descricao = Column(VARCHAR(255), nullable=False)
    valor = Column(VARCHAR(255), nullable=False)
    foto = Column(VARCHAR(255), nullable=True)  # Foto pode ser NULL
    categoria = Column(VARCHAR(50), nullable=False)
    quantidade_em_estoque = Column(Integer, nullable=False)
    ativo = Column(Boolean, default=True)  # Valor padrão é True (ativo)

    def __init__(self, id_produto, nome, descricao, valor, foto, categoria, quantidade_em_estoque, ativo=True):
        self.id_produto = id_produto
        self.nome = nome
        self.descricao = descricao
        self.valor = valor
        self.foto = foto
        self.categoria = categoria
        self.quantidade_em_estoque = quantidade_em_estoque
        self.ativo = ativo
