from typing import Optional
from pydantic import BaseModel as SCBaseModel

class CreateUserSchema(SCBaseModel):
    """Classe voltada para represnetar o schema de registro de um usuário.

    """
    nome: str  # nome do usuário

    class Config:
        orm_mode: True
        
class UpdateUserSchema(SCBaseModel):
    """Classe que modela o schema de atualização de um usuário.

    """
    
    user_id: int  # id do usuário
    nome: str     # nome do usuário

    class Config:
        orm_mode: True