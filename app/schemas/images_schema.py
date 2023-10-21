from pydantic import BaseModel as SCBaseModel


class GetImageSchema(SCBaseModel):
    """Classe que representa o schema para buscar uma imagem.

    """
    user_id: int    # chave da tebela de usuários
    image_id: int   # id da imagem    

    class Config:
        orm_mode = True


class CreateImageSchema(SCBaseModel):
    """Classe voltada para representar o schema de registro de uma imagem.

    """
    user_id: int     # chave da tebela de usuários
    b64image: str    # imagem em formato base 64    
    
    class Config:
        orm_mode = True


class UpdateImageSchema(SCBaseModel):
    """Classe que representa o schema para atualizar uma imagem.

    """
    user_id: int    # chave da tebela de usuários
    image_id: int   # id da imagem
    b64image: str   # imagem em formato base 64    
           
    class Config:
        orm_mode = True


class DeleteImageSchema(SCBaseModel):
    """Classe que representa o schema para deletar uma imagem.

    """
    user_id: int   # chave da tebela de usuários
    image_id: int  # id da imagem    

    class Config:
        orm_mode = True


class GetImagesThumbsSchema(SCBaseModel):
    """Classe que representa o schema para recuperar imagens em formato thumbnail.
    """ 
    user_id: int  # chave da tebela de usuários

    class Config:
        orm_mode = True