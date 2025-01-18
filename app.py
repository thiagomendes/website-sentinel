import requests
import hashlib
import time
from bs4 import BeautifulSoup
from flask import Flask, render_template, send_from_directory
from threading import Thread

app = Flask(__name__)

# Constantes
CHECK_INTERVAL = 300  # Intervalo em segundos para verificar o site

# Dados globais
site_url = "http://127.0.0.1:5000/fake-site.html"  # URL do site simulado
data_storage = []  # Armazena tentativas de verificação
last_hash = None

# Cabeçalhos para simular um navegador
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

def fetch_site_content():
    """Busca o conteúdo do site usando um cabeçalho User-Agent."""
    try:
        response = requests.get(site_url, headers=headers)
        response.raise_for_status()  # Levanta erro se a requisição falhar
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

def monitor_site():
    """Monitora o site para detectar alterações."""
    global last_hash
    while True:
        print("Verificando site...")
        html_content = fetch_site_content()
        if html_content is None:
            data_storage.append({
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
                "status": "Erro ao acessar o site",
                "hash": "N/A"
            })
            time.sleep(CHECK_INTERVAL)  # Aguarda o intervalo antes de tentar novamente
            continue

        # Extrair apenas o <body> e calcular o hash
        body_content = extract_body_content(html_content)
        current_hash = calculate_hash(body_content)

        if last_hash and current_hash != last_hash:
            print("Alteração detectada no site!")
            data_storage.append({
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
                "status": "Alteração detectada",
                "hash": current_hash
            })
        else:
            print("Nenhuma alteração detectada.")
            data_storage.append({
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
                "status": "Sem alterações",
                "hash": current_hash
            })

        last_hash = current_hash
        time.sleep(CHECK_INTERVAL)  # Aguarda o intervalo antes da próxima verificação

@app.route("/")
def index():
    """Exibe os resultados na página principal."""
    # Contar o número de alterações detectadas
    change_count = sum(1 for entry in data_storage if entry["status"] == "Alteração detectada")
    return render_template(
        "index.html",
        data=data_storage[::-1],  # Exibe os registros em ordem decrescente
        refresh_interval=CHECK_INTERVAL,
        site_url=site_url,
        change_count=change_count  # Passa o número de alterações para o template
    )

@app.route("/fake-site.html")
def fake_site():
    """Serve o arquivo HTML do site simulado."""
    return send_from_directory("./templates", "fake-site.html")

if __name__ == "__main__":
    # Inicia o monitoramento em uma thread separada
    Thread(target=monitor_site, daemon=True).start()
    # Inicia o servidor Flask
    app.run()