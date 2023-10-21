from fastapi import APIRouter

from api.v1.enpoints import root, user, user_image, user_image_thumb
from core.configs import settings

#Instanciando o Objeto API Router
api_router = APIRouter()

# Incluindo as rodas e suas respectivas Tags
api_router.include_router(root.router, tags=['root API Endpoint'])
api_router.include_router(user.router, prefix='/users', tags=['Users API Endpoint'])
api_router.include_router(user_image.router, prefix='/users-images', tags=['Users Images API Endpont'])
api_router.include_router(user_image_thumb.router, prefix='/users-images-thumbnails', tags=['Thumbnails List EntPoint API'])