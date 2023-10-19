from typing import Optional
from pydantic import BaseModel


class UserImage(BaseModel):
    """Classe voltada para representar o registro de uma imagem vinculada à um usuário. 
    
    """
    
    id: Optional [int] = None   # id da imagem
    user_id: int                # id do usário o qual a imagem está vinculada
    b64image: str               # imagem codificada em base64
