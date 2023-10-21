from fastapi import FastAPI

from core.configs import settings
from api.api import api_router


#Criando objeto FastAPI
app = FastAPI(title="User Image System - API", 
              version="0.0.5", 
              description="The User Image System - UIS is a simple API that store images of clients.")


# ------ Chamando rotas da API ---------- #
app.include_router(api_router, prefix=settings.API_V1_STR)


# Verificação padrão. Caso o arquivo .py seja o principal.
if __name__ == "__main__":
    import uvicorn
    
    # Inicializando a aplicação
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info", reload=True)