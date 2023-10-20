from typing import List

from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.users_model import UserModel
from schemas.users_schema import UserSchema
from core.deps import get_session
from core.configs import settings

# Instancia um objeto do APIRouter
router = APIRouter()


@router.post('', status_code=status.HTTP_201_CREATED)
async def create_user(user: UserSchema, db: AsyncSession = Depends(get_session)):
    """Rota que cadastra um novo usuário.
    
    Corresponde à seção dos requisitos:
        - /add-user
            - request : receives a User Name
            - response: returns the new User ID.
    
    Keyword arguments:
        user -- Recebe um Json contendo o nome de usuário como argumento
        Return: Novo ID de usuário cadastrado
    """
        
    new_user = UserModel(nome = user.nome)

    db.add(new_user)
    await db.commit()

    return new_user.id


@router.put('/{user_id}', status_code=status.HTTP_201_CREATED)
async def update_user(user_id: int, user: UserSchema, db: AsyncSession = Depends(get_session)):
    """Rota que atualiza um usuário já cadastrado.

    Corresponde à seção dos requisitos:
        - /update-user
            - request : receives a User ID and new User Name
            - response: returns the User ID.
    
    Keyword arguments:
    user_id -- ID de usuário a ser alterado.
    Return: Retorna o ID do usuário que foi atualizado.
    """
    
    async with db as session:
        query = select(UserModel).filter(UserModel.id == user_id)
        result = await session.execute(query)
        user_update =  result.scalar_one_or_none()

        if user_update:
            user_update.nome = user.nome
            
            await session.commit()

            return user_update.id
        
        else:
            raise HTTPException(detail='Usuário não encontrada.',
                                status_code=status.HTTP_404_NOT_FOUND)
