from typing import Optional
from pydantic import BaseModel as SCBaseModel

class UserSchema(SCBaseModel):
    """Classe voltada para represnetar o schema de registro de um usuário.

    """
    
    id: Optional [int]  # id do usuário
    nome: str           # nome do usuário

    def __repr__(self) -> str:
        return f'id: {self.id}\n nome: {self.nome}'
    
