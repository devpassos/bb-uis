import sqlalchemy as sa
from typing import Optional
from pydantic import BaseModel

class Image(BaseModel):
    """Classe voltada para representar o registro de uma imagem.

    """
    __tablename__: str = 'images'

    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)  # id da imagem registrado no banco
    user_id: int = sa.ForeignKey()
    b64image: str = sa.Column(sa.Text, nullable=False)                        # imagem em formato base 64

    def __repr__(self) -> str:
        return f'id: {self.id} \nb64image: {self.b64image}'
