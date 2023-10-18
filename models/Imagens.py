from typing import Optional
from pydantic import BaseModel

class Image(BaseModel):
    """Classe voltada para representar o registro de uma imagem.

    """

    id: Optional [int] = None   # id da imagem registrado no banco
    b64image: str               # imagem em formato base 64

