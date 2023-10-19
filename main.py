from fastapi import FastAPI, HTTPException
from typing import Optional, List
from api.v1.endpoints import root


#Criando objeto FastAPI
app = FastAPI(title="User Image System - API", 
              version="0.0.2", 
              description="The User Image System - UIS is a simple API that store images of clients.")


# ------ Rota default ---------- #
app.include_router(route_raiz.router, tags=['default'])

# ------ Rotas relacionadas à usuáros ---------- #
app.include_router(route_users.router, tags=['users'])


# ------ Rotas relacionadas à usuários x imagens ---------- #
app.include_router(route_users_images.router, tags=['users-images'])


# Verificação padrão. Caso o arquivo .py seja o principal.
if __name__ == "__main__":
    import uvicorn
    
    # Inicializando a aplicação
    uvicorn.run("main:app", host="0.0.0.0", port=9192, log_level="info", reload=True)