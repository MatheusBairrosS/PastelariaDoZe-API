from fastapi import APIRouter
from domain.entities.Funcionario import Funcionario

router = APIRouter()

# Criar as rotas/endpoints: GET, POST, PUT, DELETE

@router.get("/funcionario/", tags=["Funcionario"])
def get_funcionario():  
    return {"msg": "get todos executado"}, 200

@router.get("/funcionario/{id}", tags=["Funcionario"])
def get_funcionario(id: int):
    return {"msg": "get um executado"}, 200

@router.post("/funcionario/", tags=["Funcionario"])
def post_funcionario(corpo: Funcionario):
    return {"msg": "post executado"}, 200

@router.put("/funcionario/{id}", tags=["Funcionario"])
def put_funcionario(id: int):
    return {"msg": "put executado"}, 200

@router.delete("/funcionario/{id}", tags=["Funcionario"])
def delete_funcionario(id: int):
    return {"msg": "delete executado"}, 200