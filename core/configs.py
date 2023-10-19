import os

from typing import List
from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base



class Settings(BaseSettings):
    """Configurações gerais do projeto
    
    """
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'sqlite+aiosqlite:///db/uis.sqlite'
    DB_BASE_MODEL = declarative_base()

    class Config:
        case_sensitive = True


settings = Settings()