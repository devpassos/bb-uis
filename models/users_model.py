import sqlalchemy as sa
from core.configs import settings
from sqlalchemy import Column, Integer, String



class UserModel(settings.DB_BASE_MODEL):
    """Classe voltada para represnetar o registro de um usuário.

    """

    __tablename__: str = "users"
    
    id: int = Column(Integer, primary_key=True, autoincrement=True)   # id do usuário
    nome: str = Column(String(50), nullable=False)                    # nome do usuário

    def __repr__(self) -> str:
        return f'id: {self.id}\n nome: {self.nome}'
    
