from typing import Optional
from pydantic import BaseModel as SCBaseModel


class ImageSchema(SCBaseModel):
    """Classe voltada para representar o schema de registro de uma imagem.

    """

    id: Optional [int] # id da imagem registrado no banco
    b64image: str      # imagem em formato base 64    
    user_id: int       # chave da tebela de usuários

    class config:
        orm_mode = True


    def __repr__(self) -> str:
        return f'id: {self.id} \nb64image: {self.b64image}'
