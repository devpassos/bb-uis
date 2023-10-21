from PIL import Image
import io
import base64

def base64_image_resize(base64_string, new_width=100, new_height=100):
    try:
        # Decodifica a imagem base64 para dados binários
        image_data = base64.b64decode(base64_string)
        
        # Abre a imagem usando o PIL
        image = Image.open(io.BytesIO(image_data))
        
        # Redimensiona a imagem mantendo a proporção
        image.thumbnail((new_width, new_height))
        
        # Converte a imagem redimensionada de volta para base64
        buffered = io.BytesIO()
        image.save(buffered, format="JPEG")
        base64_resized_string = base64.b64encode(buffered.getvalue()).decode("utf-8")
        
        return base64_resized_string
    
    except Exception as error:
        return f'Erro ao redimensionar a imagem base64: {str(error)}'


