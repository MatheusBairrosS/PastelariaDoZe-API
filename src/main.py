#Matheus Bairros Silva
from fastapi import FastAPI
from settings import HOST, PORT, RELOAD
import uvicorn
# import das classes com as rotas/endpoints
from app import FuncionarioDAO
from app import ClienteDAO
from app import ProdutoDAO
app = FastAPI()
# mapeamento das rotas/endpoints
app.include_router(FuncionarioDAO.router)
app.include_router(ClienteDAO.router)
app.include_router(ProdutoDAO.router)
if __name__ == "__main__":
    uvicorn.run("main:app", host=HOST, port=int(PORT), reload=RELOAD)