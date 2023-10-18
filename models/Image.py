from typing import Optional
from pydantic import BaseModel

class Image(BaseModel):
    """
    Classe voltada para representar o registro de uma imagem no banco de dados.

    """
    id: [int] # id da imagem registrado no banco
    b64image: [str] # imagem em formato base 64
    valid: Optional[bool] # Se a imagem é valida ou não. 


