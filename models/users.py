import sqlalchemy as sa
from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    """Classe voltada para represnetar o registro de um usuário.

    """

    __tablename__: str = "users"
    
    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)   # id do usuário
    nome: str = sa.Column(sa.String(50), nullable=False)                                       # nome do usuário

    def __repr__(self) -> str:
        return f'id: {self.id}\n nome: {self.nome}'
    
