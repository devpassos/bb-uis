import sqlalchemy as sa
import sqlalchemy.orm as orm
from core.configs import settings
from models.users_model import UserModel
from sqlalchemy import Column, Integer, String, Text, ForeignKey


class ImageModel(settings.DB_BASE_MODEL):
    """Classe voltada para representar o registro de uma imagem.

    """
    __tablename__: str = 'images'

    id: int = Column(Integer, primary_key=True, autoincrement=True)  # id da imagem registrado no banco
    b64image: str = Column(Text, nullable=False)                     # imagem em formato base 64
    
    user_id: int = Column(Integer, ForeignKey('users.id'))           # chave da tebela de usuários
    user: UserModel = orm.relationship('User', lazy='joined')        # join com a tabela de usuários

    def __repr__(self) -> str:
        return f'id: {self.id} \nb64image: {self.b64image}'
