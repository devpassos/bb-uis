# Imagem de referêcia pyrhon 3.9
FROM python:3.9

# Diretório padrão de trabalho
WORKDIR /app

# Copia arquivo de requisitos para o diretório de trabalho
COPY /app ./

# Instalação dos pacotes requeridos
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Criando banco de dados
RUN python -m criar_tabelas

# Exponto portas para conexão Web
EXPOSE 8000

# Executando aplicação ao inicializar o container
CMD [ "gunicorn", "main:app", "-w", "4", "-k", "uvicorn.workers.UvicornWorker" ]