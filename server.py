from flask import Flask, render_template
import sqlite3
import config  # Importa as configurações compartilhadas

app = Flask(__name__)

def get_data():
    """Obtém os dados do banco SQLite."""
    conn = sqlite3.connect(config.DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT timestamp, status, hash FROM site_data ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()
    return [{"timestamp": row[0], "status": row[1], "hash": row[2]} for row in rows]

@app.route("/")
def index():
    """Exibe os resultados na página principal."""
    data_storage = get_data()
    change_count = sum(1 for entry in data_storage if entry["status"] == "Alteração detectada")
    return render_template(
        "index.html",
        data=data_storage,
        refresh_interval=config.CHECK_INTERVAL,
        site_url=config.SITE_URL,
        change_count=change_count
    )

if __name__ == "__main__":
    app.run()
