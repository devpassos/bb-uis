import os
from core.configs import settings
from core.database import engine


async def create_tables() -> None:
    import models.all_models

    if not os.path.exists('db'):
        print('Criando Banco de dados...')
        os.mkdir('db')
    

    print('Abrindo Conexão com o banco de dados...')

    async with engine.begin() as conn:
        print('apagando as tabelas do banco de dados caso existam...')
        await conn.run_sync(settings.DB_BASE_MODEL.metadata.drop_all)
        print('Criando as tabelas da aplicação...')
        await conn.run_sync(settings.DB_BASE_MODEL.metadata.create_all)
    
    print('Finalizando a criação das tabelas...')


if __name__ == '__main__':
    import asyncio

    asyncio.run(create_tables())