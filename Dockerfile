# Imagem de referêcia pyrhon 3.11
FROM python:3.11

# Diretório padrão de trabalho
WORKDIR /app

# Copia arquivo de requisitos para o diretório de trabalho
COPY ./ ./

# Instalação dos pacotes requeridos
RUN pip install --no-cache-dir -r requirements.txt

# Definição de variáveis de ambiente necessárias
#ENV KEY Value

# Executando aplicação ao inicializar o container
CMD [ "uvicorn", "main:app" ]