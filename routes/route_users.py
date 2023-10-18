from fastapi import APIRouter
from models.Usuarios import User

router = APIRouter()

@router.get('/api/v1/users')
async def create_user(user: User):
    """Rota que cadastra um novo usuário.
    
    Corresponde à seção dos requisitos:
        - /add-user
            - request : receives a User Name
            - response: returns the new User ID.
    
    Keyword arguments:
        user -- Recebe um Json contendo o nome de usuário como argumento
        Return: Novo ID de usuário cadastrado
    """
    
    return user.id

@router.post('/api/v1/users/{user_id}')
async def update_user(user_id: int, user: User):
    """Rota que atualiza um usuário já cadastrado.

    Corresponde à seção dos requisitos:
        - /update-user
            - request : receives a User ID and new User Name
            - response: returns the User ID.
    
    Keyword arguments:
    user_id -- ID de usuário a ser alterado.
    Return: Retorna o ID do usuário que foi atualizado.
    """
    
    return {
        "user_id": 0
    }