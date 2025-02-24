#Matheus Bairros Silva
from pydantic import BaseModel

class Produto(BaseModel):
    id_Produto: int = None
    nome: str
    descricao: str
    valor: str
    foto: str = None
    categoria: str
    quantidade_em_estoque: int
    ativo: bool = True
