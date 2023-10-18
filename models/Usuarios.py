from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    """Classe voltada para represnetar o registro de um usuário.

    """

    id: Optional [int] = None   # id do usuário
    nome: str                   # nome do usuário

