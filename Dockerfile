# Use uma imagem base Python
FROM python:3.12-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos necessários para o container
COPY requirements.txt ./requirements.txt
COPY monitor.py ./monitor.py
COPY server.py ./server.py
COPY config.py ./config.py
COPY templates/ ./templates/

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Exponha a porta usada pela aplicação
EXPOSE 5000

# Comando para iniciar o monitoramento e o servidor
CMD ["sh", "-c", "python monitor.py & python server.py"]
