#Matheus Bairros Silva
from fastapi import APIRouter
from domain.entities.Produto import Produto

# import da persistência
import db
from infra.orm.ProdutoModel import ProdutoDB

# import da segurança
from typing import Annotated
from fastapi import Depends
from security import get_current_active_user, User

router = APIRouter(dependencies=[Depends(get_current_active_user)])

# Criar os endpoints de Cliente: GET, POST, PUT, DELETE

# Rota para buscar todos os produtos
@router.get("/produto/", tags=["Produto"], dependencies=[Depends(get_current_active_user)], )
async def get_produto():
    try:
        session = db.Session()
        # Busca todos os produtos
        dados = session.query(ProdutoDB).all()
        return dados, 200
    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close()

# Rota para buscar um produto específico pelo ID
@router.get("/produto/{id}", tags=["Produto"])
async def get_produto(id: int):
    try:
        session = db.Session()
        # Busca um produto com filtro pelo id
        dados = session.query(ProdutoDB).filter(ProdutoDB.id_produto == id).all()
        return dados, 200
    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close()

# Rota para criar um novo produto
@router.post("/produto/", tags=["Produto"])
async def post_produto(corpo: Produto):
    try:
        session = db.Session()
        # Cria um novo produto com os dados da requisição
        dados = ProdutoDB(None, corpo.nome, corpo.descricao, corpo.valor, corpo.foto,
                          corpo.categoria, corpo.quantidade_em_estoque, corpo.ativo)
        
        session.add(dados)
        session.commit()
        return {"id": dados.id_produto}, 200
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()

# Rota para atualizar um produto existente
@router.put("/produto/{id}", tags=["Produto"])
async def put_produto(id: int, corpo: Produto):
    try:
        session = db.Session()
        # Busca os dados atuais pelo id
        dados = session.query(ProdutoDB).filter(ProdutoDB.id_produto == id).one()
        # Atualiza os dados com base no corpo da requisição
        dados.nome = corpo.nome
        dados.descricao = corpo.descricao
        dados.valor = corpo.valor
        dados.foto = corpo.foto
        dados.categoria = corpo.categoria
        dados.quantidade_em_estoque = corpo.quantidade_em_estoque
        dados.ativo = corpo.ativo
        session.add(dados)
        session.commit()
        return {"id": dados.id_produto}, 200
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()

# Rota para deletar um produto pelo ID
@router.delete("/produto/{id}", tags=["Produto"])
async def delete_produto(id: int):
    try:
        session = db.Session()
        # Busca os dados atuais pelo id
        dados = session.query(ProdutoDB).filter(ProdutoDB.id_produto == id).one()
        session.delete(dados)
        session.commit()
        return {"id": dados.id_produto}, 200
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()

# Rota para buscar produtos por categoria
@router.get("/produto/categoria/{categoria}", tags=["Produto - Buscar por Categoria"])
async def get_produto_por_categoria(categoria: str):
    try:
        session = db.Session()
        # Busca produtos com filtro pela categoria
        dados = session.query(ProdutoDB).filter(ProdutoDB.categoria == categoria).all()
        return dados, 200
    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close()

# Rota para buscar se um produto já existe no sistema pela categoria e nome
@router.get("/produto/existe/{nome}/{categoria}", tags=["Produto - Verifica se Produto Existe"])
async def produto_existe(nome: str, categoria: str):
    try:
        session = db.Session()
        # Verifica se o produto existe pela combinação de nome e categoria
        dados = session.query(ProdutoDB).filter(ProdutoDB.nome == nome).filter(ProdutoDB.categoria == categoria).all()
        return dados, 200
    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close()