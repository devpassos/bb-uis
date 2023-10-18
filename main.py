from fastapi import FastAPI, HTTPException
from typing import Optional, List
from routes import route_raiz, route_users, route_users_images


#Criando objeto FastAPI
app = FastAPI(title="User Image System - API", 
              version="0.0.2", 
              description="The User Image System - UIS is a simple API that store images of clients.")


# ------ Rota default ---------- #
app.include_router(route_raiz.router, tags=['default'])

# ------ Rotas relacionadas à usuáros ---------- #
#@app.post("/users", summary="Cria um usuário", status_code=status.HTTP_201_CREATED, response_model=User)
#@app.put("/users/{user_id}", summary="Atualiza o registro de um usuário existente.")
app.include_router(route_users.router, tags=['users'])


# ------ Rotas relacionadas à usuários x imagens ---------- #
#@app.get("/users-images/{user_id}/images/{image_id}", summary="Retorna uma imagem relacioada à um usuário")
#@app.post("/users-images/{user_id}")
#@app.put("/users-images/{user_id}/images/{image_id}")
#@app.delete("/users-image/{user_id}/{image_id}")
#@app.get("/users-images-thumbnails/{user_id}")

app.include_router(route_users_images.router, tags=['users-images'])


# Verificação padrão. Caso o arquivo .py seja o principal.
if __name__ == "__main__":
    import uvicorn
    
    # Inicializando a aplicação
    uvicorn.run("main:app", host="0.0.0.0", port=9192, log_level="info", reload=True)