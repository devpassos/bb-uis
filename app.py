from fastapi import FastAPI

#Criando objeto FastAPI
app = FastAPI()

@app.get('/')
async def raiz():
    """_summary_
            Método raiz padrão da API
    """
    return {
        "msg": "Olá eu sou uma mensagem de retorno do endpoint raiz"
    }

# Verificação padrão. Caso o arquivo .py seja o principal.
if __name__ == "__main__":
    import uvicorn
    
    # Inicializando a aplicação
    uvicorn.run("app:app", host="0.0.0.0", port=9192, log_level="info", reload=True)