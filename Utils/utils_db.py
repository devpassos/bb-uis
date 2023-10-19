import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext import declarative
from sqlalchemy.future.engine import Engine

from typing import Optional
from pathlib import Path


ModelBase = declarative.declarative_base()

__engine = Optional [Engine] = None

def create_engine() -> Engine:
    """Função que configura a conexão com o banco de dados

    Returns:
        Engine: Objeto do tipo Engine
    """
    global __engine
    
    if __engine:
        return
    else:
        arquivo_db = 'db/uis.sqlite'
        folder = Path(arquivo_db).parent
        folder.mkdir(parents=True, exist_ok=True)
        
        conn_str = f'sqlite:///{arquivo_db}'
        __engine = sa.create_engine(url=conn_str, echo=False, connect_args={'check_same_thread': False})
    
    return __engine


def create_session() -> Session:
    """Função que cria uma sessão com o banco de dados.

    Returns:
        Session: Retorna um objeto de sessão
    """
    global __engine
    
    if not __engine:
        create_engine()
    
    __session = sessionmaker(__engine, expire_on_commit=False, class_=Session)
    
    return __session()


def create_tables() -> None:
    """Função que limpa o banco de dados e recria todas as tabelas.
    
    """
    global __engine
    
    if not __engine:
        create_engine()
    
    import models.Usuarios
    ModelBase.metada.drop_all(__engine)
    ModelBase.metada_create_all(__engine)