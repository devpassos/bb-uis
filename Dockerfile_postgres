# Imagem de referêcia pyrhon 3.11
FROM postgres:10.19-alpine

# Diretório padrão de trabalho
WORKDIR /app

# Copia arquivo de requisitos para o diretório de trabalho
#COPY requirements.txt ./

# Instalação dos pacotes requeridos
#RUN pip install --no-cache-dir -r requirements.txt

# Definição de variáveis de ambiente necessárias
ENV POSTGRES_PASSWORD "password" POSTGRES_HOST_AUTH_METHOD "trust"

# Executando aplicação ao inicializar o container
#CMD [ "ls", "-lah" ]