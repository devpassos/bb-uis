from typing import List

from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.images_model import ImageModel
from schemas.images_schema import GetImagesThumbsSchema

from core.deps import get_session
from core.configs import settings
from core.util import base64_image_resize


router = APIRouter()


@router.get('', status_code=status.HTTP_200_OK)
async def read_users_images_thumb(get_thumb: GetImagesThumbsSchema, db: AsyncSession= Depends(get_session)):
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
        list_resized_images: List[str] = []
        
        try:
            query = select(ImageModel).filter(ImageModel.user_id == get_thumb.user_id)
            result = await session.execute(query)
            images: List[ImageModel] =  result.scalars().all()
            
            if images:
                for img in images:
                    # redimensionando as imagens do dos usuários:
                    base64_string = img.b64image
                    base64_resized_string = base64_image_resize(base64_string)

                    if  not base64_resized_string.startswith("Erro"):
                        list_resized_images.append(base64_resized_string)
                    else:
                        continue

                return list_resized_images
            
            return Response(status_code=status.HTTP_404_NOT_FOUND)
            
        except HTTPException as error:
                error(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)