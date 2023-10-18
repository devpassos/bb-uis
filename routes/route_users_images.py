from fastapi import APIRouter, status
from models.Imagens import Image


router = APIRouter()


@router.get('/api/v1/users-images/{user_id}/images/{image_id}')
async def get_user_image(user_id: int, image_id: int):
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
    
    pass


@router.post('/api/v1/users-images/{user_id}')
async def create_user_image(user_id: int, image: Image):
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
    
    return image


@router.put('/api/v1/users-images/{user_id}/images/{image_id}')
async def update_user_image(user_id: int, image_id: int, image: Image):
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
    
    return (status.HTTP_204_NO_CONTENT)


@router.delete('/api/v1/users-image/{user_id}/images/{image_id}')
async def delete_user_image(user_id: int, image_id: int):
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
    pass


router.get('/api/v1/users-images-thumbnails/{user_id}')
async def read_users_images_thumb(user_id: int):
    """Rota que lista todas as imagens relacionadas à um usuário.
    
    Corresponde à sessão de requisitos:
        - /list-user-images-thumbnails
            - request : receives a User ID
            - response: return a list of user's images ID and (Base 64 Format) on maximum size of 100x100, and preserving aspect ratio.

    Keyword arguments:
    user_id  -- ID de usuário.
    Return: Retorna uma lista de representações em base64 das imagens dos usuários limitando o tamanho da representação em 100x100, mantidas as proporções.
    """
    pass