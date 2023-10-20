from typing import List

from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.images_model import ImageModel
from schemas.images_schema import ImageSchema

from core.deps import get_session
from core.configs import settings


router = APIRouter()


router.get('/{user_id}')
async def read_users_images_thumb(user_id: int, db: AsyncSession= Depends(get_session)):
    """Rota que lista todas as imagens relacionadas à um usuário.
    
    Corresponde à sessão de requisitos:
        - /list-user-images-thumbnails
            - request : receives a User ID
            - response: return a list of user's images ID and (Base 64 Format) on maximum size of 100x100, and preserving aspect ratio.

    Keyword arguments:
    user_id  -- ID de usuário.
    Return: Retorna uma lista de representações em base64 das imagens dos usuários limitando o tamanho da representação em 100x100, mantidas as proporções.
    """
    async with db as session:
        query = select(ImageModel).filter(ImageModel.user_id == user_id)
        result = await session.execute(query)
        images: List[ImageModel] =  result.scalars().all()

        if images:
            return images
        else:
            raise HTTPException(detail='Nenhuma imagem encontrada para este usuário.',
                                status_code=status.HTTP_404_NOT_FOUND)