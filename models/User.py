from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    """
    Classe voltada para represnetar o registro de um usuário.

    """
    id: [int]  #id do usuário
    nome: [str] #nome do usuário
    sobrenome: Optional[str] # sobrenome do usuário

