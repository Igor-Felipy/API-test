from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()

# Rota Raiz 
@app.get("/")
def raiz():
    return {"Ola":"Mundo"}


# Criar model 
class Usuario(BaseModel):
    id: int
    email: str 
    senha: str


# Criar base de dados

base_de_dados = [
    Usuario(id=1, email="igor@igor.com", senha="roger123"),
    Usuario(id=2, email="teste@teste.com", senha="teste@123")
]


# Rota get All 

@app.get("/usuarios")
def get_todos_os_usuarios():
    return base_de_dados

# Rota get ID 
@app.get("/usuarios/{id_usuario}")
def get_usuario_usando_id(id_usuario: int):
    for usuario in base_de_dados:
        if(usuario.id == id_usuario):
            return usuario
    
    return {"Status":404, "Mensagem": "Não encontrou usuario"}

# Rota insere
@app.post("/usuarios")
def insere_usuario(Usuario:Usuario):
    # criar regras de negocio
    base_de_dados.append(Usuario)
    return Usuario