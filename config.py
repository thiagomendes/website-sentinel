# config.py

# URL do site a ser monitorado
SITE_URL = "https://iaa.ufpr.br/iaa2025-processo-seletivo-para-ingresso-na-iaa/"

# Cabeçalhos para simular um navegador
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

# Banco de dados SQLite
DATABASE = "data_storage.db"

# Intervalo de verificação do site em segundos
CHECK_INTERVAL = 300