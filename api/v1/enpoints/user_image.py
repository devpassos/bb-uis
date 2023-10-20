from typing import List

from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.images_model import ImageModel
from schemas.images_schema import ImageSchema

from core.deps import get_session
from core.configs import settings


router = APIRouter()

@router.get('/{user_id}/images/{image_id}')
async def get_user_image(user_id: int, image_id: int, db: AsyncSession = Depends(get_session)):
    """Rota que busca uma imagem relacioada à um usuário
    
    Corresponde à seção dos requisitos:
        - /get-user-image
            - request : receives a User ID and an Image ID.
            - response: returns requested image (Base 64 Format).
    
    Keyword arguments:
    user_id  -- ID de usuário.
    image_id -- ID da imagem.
    Return: Retorna a representação em base64 da imagem requisitada.
    """
    async with db as session:
        query = select(ImageModel).filter(ImageModel.user_id == user_id).filter(ImageModel.id == image_id)
        result = await session.execute(query)
        image =  result.scalar_one_or_none()

        if image:
            return image.b64image
        else:
            raise HTTPException(detail='Imagem não encontrada.',
                                status_code=status.HTTP_404_NOT_FOUND)

    


@router.post('/{user_id}', status_code=status.HTTP_201_CREATED)
async def create_user_image(user_id: int, image: ImageSchema, db: AsyncSession = Depends(get_session)):
    """Rota que registra uma imagem vinculando-a à um ID de usuário.
    
    Corresponde à sessão de requisitos:
        - /add-user-image
            - request : receives a User ID and an image (Base 64 Format).
            - response: returns the new image ID.

    
    Keyword arguments:
    user_id -- ID de usuário
    image   -- Json com a representação da imagem em base 64  
    Return: retorna o ID da imagem cadastrada.
    """
    
    new_user_image = ImageModel(user_id= user_id, b64image = image.b64image)

    db.add(new_user_image)
    await db.commit()

    return new_user_image.id


@router.put('/{user_id}/images/{image_id}', status_code=status.HTTP_204_NO_CONTENT)
async def update_user_image(user_id: int, image_id: int, image: ImageSchema, db: AsyncSession = Depends(get_session)):
    """Rota que atualiza uma imagem já cadastrada anteriormente.
    
    Corresponde à sessão de requisitos:
        - /update-user-image
            - request : receives a User ID, an Image ID, and a new image (Base 64 Format)
            - response : no response body needed

    Keyword arguments:
    user_id  -- ID de usuário.
    image_id -- ID da imagem.
    image    -- Json com a representação da imagem em base 64. 
    Return: sem retorno.
    """
    
    async with db as session:
        query = select(ImageModel).filter(ImageModel.user_id == user_id).filter(ImageModel.id == image_id)
        result = await session.execute(query)
        image_update =  result.scalar_one_or_none()

        if image_update:
            image_update.b64image = image.b64image
            
            await session.commit()

            return Response(status_code=status.HTTP_204_NO_CONTENT)
        
        else:
            raise HTTPException(detail='Imagem não encontrada.',
                                status_code=status.HTTP_404_NOT_FOUND)




@router.delete('/{user_id}/images/{image_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_user_image(user_id: int, image_id: int, db: AsyncSession = Depends(get_session)) :
    """Rota que deleta uma imagem relacionada à um usuário cadastrado.
    
    Corresponde à sessão de requisitos:
        - /delete-user-image
            - request : receives a User ID and an Image ID
            - response: no response body needed

    Keyword arguments:
    user_id  -- ID de usuário.
    image_id -- ID da imagem.    Return: return_description
    Return: Sem retorno.
    """
    async with db as session:
        query = select(ImageModel).filter(ImageModel.user_id == user_id).filter(ImageModel.id == image_id)
        result = await session.execute(query)
        image_delete =  result.scalar_one_or_none()

        if image_delete:
            await session.delete(image_delete)
            
            await session.commit()

            return Response(status_code=status.HTTP_204_NO_CONTENT)
        
        else:
            raise HTTPException(detail='Imagem não encontrada.',
                                status_code=status.HTTP_404_NOT_FOUND)