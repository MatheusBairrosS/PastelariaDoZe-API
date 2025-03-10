#Matheus Bairros Silva
from fastapi import APIRouter
from domain.entities.Cliente import Cliente

# import da persistência
import db
from infra.orm.ClienteModel import ClienteDB

router = APIRouter()

# Criar os endpoints de Cliente: GET, POST, PUT, DELETE

@router.get("/cliente/", tags=["Cliente"])
async def get_cliente():
    try:
        session = db.Session()
        # Busca todos os funcionários
        dados = session.query(ClienteDB).all()
        return dados, 200
    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.get("/cliente/{id}", tags=["Cliente"])
async def get_cliente(id: int):
    try:
        session = db.Session()
        # Busca um cliente com filtro pelo id
        dados = session.query(ClienteDB).filter(ClienteDB.id_cliente == id).all()
        return dados, 200
    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.post("/cliente/", tags=["Cliente"])
async def post_cliente(corpo: Cliente):
    try:
        session = db.Session()
        # Cria um novo cliente com os dados da requisição
        dados = ClienteDB(None, corpo.nome, corpo.cpf, corpo.telefone)
        
        session.add(dados)
        session.commit()
        return {"id": dados.id_cliente}, 200
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.put("/cliente/{id}", tags=["Cliente"])
async def put_cliente(id: int, corpo: Cliente):
    try:
        session = db.Session()
        # Busca os dados atuais pelo id
        dados = session.query(ClienteDB).filter(ClienteDB.id_cliente == id).one()
        # Atualiza os dados com base no corpo da requisição
        dados.nome = corpo.nome
        dados.cpf = corpo.cpf
        dados.telefone = corpo.telefone
        session.add(dados)
        session.commit()
        return {"id": dados.id_cliente}, 200
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.delete("/cliente/{id}", tags=["Cliente"])
async def delete_cliente(id: int):
    try:
        session = db.Session()
        # Busca os dados atuais pelo id
        dados = session.query(ClienteDB).filter(ClienteDB.id_cliente == id).one()
        session.delete(dados)
        session.commit()
        return {"id": dados.id_cliente}, 200
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.post("/cliente/login/", tags=["Cliente - Login"])
async def login_cliente(corpo: Cliente):
    try:
        session = db.Session()
        # Verifica o CPF e a senha informados pelo usuário
        dados = session.query(ClienteDB).filter(ClienteDB.cpf == corpo.cpf).one()
        if dados:
            # Se houver um resultado válido, retorna os dados
            return dados, 200
        else:
            return {"erro": "CPF ou senha inválidos!"}, 400
    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.get("/cliente/cpf/{cpf}", tags=["Cliente - Valida CPF"])
async def cpf_cliente(cpf: str):
    try:
        session = db.Session()
        # Verifica se o CPF já está cadastrado
        dados = session.query(ClienteDB).filter(ClienteDB.cpf == cpf).all()
        return dados, 200
    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close()
