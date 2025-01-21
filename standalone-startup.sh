#!/bin/bash

# Atualizar pacotes do sistema
echo "Atualizando pacotes do sistema..."
sudo apt update && sudo apt upgrade -y

# Instalar dependências essenciais
echo "Instalando dependências essenciais..."
sudo apt install -y python3 python3-venv python3-pip git

# Clonar o repositório da aplicação
echo "Clonando o repositório..."
if [ ! -d "website-sentinel" ]; then
    git clone https://github.com/thiagomendes/website-sentinel.git
else
    echo "Repositório já existe. Atualizando..."
    cd website-sentinel
    git pull
    cd ..
fi

# Navegar para o diretório da aplicação
cd website-sentinel

# Criar e ativar o ambiente virtual
echo "Criando e ativando o ambiente virtual..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi
source venv/bin/activate

# Instalar as dependências da aplicação
echo "Instalando dependências da aplicação..."
pip install --no-cache-dir -r requirements.txt

# Certificar-se de que a porta 5000 está aberta
echo "Abrindo a porta 5000 no firewall..."
sudo ufw allow 5000 || echo "A porta 5000 já está aberta."

# Rodar o monitor em segundo plano
echo "Iniciando o monitoramento..."
nohup python monitor.py > monitor.log 2>&1 &

# Rodar o servidor Flask
echo "Iniciando o servidor Flask..."
nohup python server.py > server.log 2>&1 &

# Informar ao usuário que a aplicação está rodando
echo "A aplicação está rodando!"
echo "Monitor logs: website-sentinel/monitor.log"
echo "Server logs: website-sentinel/server.log"
echo "Acesse a aplicação em http://<IP_PUBLICO>:5000"
