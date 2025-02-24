#Matheus Bairros Silva
from fastapi import APIRouter
from domain.entities.Cliente import Cliente

router = APIRouter()

# Criar os endpoints de Cliente: GET, POST, PUT, DELETE

@router.get("/cliente/", tags=["Cliente"])
def get_cliente():
    return {"msg": "get todos executado"}, 200

@router.get("/cliente/{id}", tags=["Cliente"])
def get_cliente(id: int):
    return {"msg": "get um executado"}, 200

@router.post("/cliente/", tags=["Cliente"])
def post_cliente(corpo: Cliente):
    return {"msg": "post executado"}, 200

@router.put("/cliente/{id}", tags=["Cliente"])
def put_cliente(id: int):
    return {"msg": "put executado"}, 200

@router.delete("/cliente/{id}", tags=["Cliente"])
def delete_cliente(id: int):
    return {"msg": "delete executado"}, 200