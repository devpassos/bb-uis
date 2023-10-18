from fastapi import APIRouter, status
from models.Imagens import Image


router = APIRouter()


@router.get('/api/v1', description="Rota raiz da API", summary="Rota raiz")
async def root():
  
    return {
        "msg": "Olá eu sou uma mensagem de retorno do endpoint raiz"
    }