from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def raiz():
    return {
        "msg": "Olá eu sou uma mensagem de retorno do endpoint raiz"
    }


