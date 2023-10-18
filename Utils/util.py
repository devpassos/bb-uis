import base64



def image_to_base64(image_path):
    try:
        with open(image_path, "rb") as image_file:
            image_data = image_file.read()
            base64_data = base64.b64encode(image_data).decode("utf-8")
            return base64_data
    except Exception as e:
        return f"Erro ao converter a imagem para base64: {str(e)}"

# 
image_path = "caminho/para/imagem.jpg"
base64_data = image_to_base64(image_path)

if not base64_data.startswith("Erro"):
    print("Imagem convertida para base64 com sucesso!")
    print("Base64 Data:")
    print(base64_data)
else:
    print(base64_data)
