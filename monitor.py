import requests
import hashlib
import time
import sqlite3
from bs4 import BeautifulSoup
import config  # Importa as configurações compartilhadas

# Inicializar hash anterior
last_hash = None

def setup_database():
    """Configura o banco de dados SQLite e limpa os dados existentes."""
    conn = sqlite3.connect(config.DATABASE)
    cursor = conn.cursor()
    
    # Cria a tabela, se não existir
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS site_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            status TEXT,
            hash TEXT
        )
    """)
    
    # Limpa a tabela ao iniciar
    cursor.execute("DELETE FROM site_data")
    conn.commit()
    conn.close()

def fetch_site_content():
    """Busca o conteúdo do site usando um cabeçalho User-Agent."""
    try:
        response = requests.get(config.SITE_URL, headers=config.HEADERS)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Erro ao acessar o site: {e}")
        return None

def extract_body_content(html):
    """Extrai apenas o conteúdo do <body> do HTML."""
    try:
        soup = BeautifulSoup(html, "html.parser")
        body = soup.body
        return body.get_text(strip=True) if body else ""
    except Exception as e:
        print(f"Erro ao processar o HTML: {e}")
        return ""

def calculate_hash(content):
    """Calcula o hash SHA-256 do conteúdo."""
    return hashlib.sha256(content.encode("utf-8")).hexdigest()

def save_data(timestamp, status, hash_value):
    """Salva dados no banco SQLite."""
    conn = sqlite3.connect(config.DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO site_data (timestamp, status, hash)
        VALUES (?, ?, ?)
    """, (timestamp, status, hash_value))
    conn.commit()
    conn.close()

def monitor_site():
    """Monitora o site para detectar alterações."""
    global last_hash
    setup_database()

    while True:
        print("Verificando site...")
        html_content = fetch_site_content()
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

        if html_content is None:
            save_data(timestamp, "Erro ao acessar o site", "N/A")
            time.sleep(config.CHECK_INTERVAL)
            continue

        # Extrair apenas o <body> e calcular o hash
        body_content = extract_body_content(html_content)
        current_hash = calculate_hash(body_content)

        if last_hash and current_hash != last_hash:
            print("Alteração detectada no site!")
            save_data(timestamp, "Alteração detectada", current_hash)
        else:
            print("Nenhuma alteração detectada.")
            save_data(timestamp, "Sem alterações", current_hash)

        last_hash = current_hash
        time.sleep(config.CHECK_INTERVAL)

if __name__ == "__main__":
    monitor_site()
