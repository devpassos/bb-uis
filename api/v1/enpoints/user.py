from fastapi import APIRouter, status, Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.users_model import UserModel
from schemas.users_schema import CreateUserSchema, UpdateUserSchema
from core.deps import get_session

# Instancia um objeto do APIRouter
router = APIRouter()


@router.post('', status_code=status.HTTP_201_CREATED)
async def create_user(user: CreateUserSchema, db: AsyncSession = Depends(get_session)):
    """Rota que cadastra um novo usuário.
    
    Corresponde à seção dos requisitos:
        - /add-user
            - request : receives a User Name
            - response: returns the new User ID.
    
    Keyword arguments:
        user -- Recebe um Json contendo o nome de usuário como argumento
        Return: Novo ID de usuário cadastrado
    """
    try:  
        new_user = UserModel(nome = user.nome)

        db.add(new_user)
        await db.commit()

        return new_user.id
    
    except HTTPException as error:
        error(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@router.put('', status_code=status.HTTP_201_CREATED)
async def update_user(user: UpdateUserSchema, db: AsyncSession = Depends(get_session)):
    """Rota que atualiza um usuário já cadastrado.

    Corresponde à seção dos requisitos:
        - /update-user
            - request : receives a User ID and new User Name
            - response: returns the User ID.
    
    Keyword arguments:
    user_id -- ID de usuário a ser alterado.
    Return: Retorna o ID do usuário que foi atualizado.
    """
    try:
        async with db as session:
            query = select(UserModel).filter(UserModel.id == user.user_id)
            result = await session.execute(query)
            user_update =  result.scalar_one_or_none()

            if user_update:
                user_update.nome = user.nome
                await session.commit()

                return user_update.id
                
            return 0
            
    except HTTPException as error:
        error(status_code=status.HTTP_404_NOT_FOUND)