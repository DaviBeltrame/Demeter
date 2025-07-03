import os
import sqlite3
from pathlib import Path

# Converter para caminho UNC (evita problemas com acentos)
caminho_absoluto = Path.home() / "Documents" / "IA" / "Demeter" / "data" / "gado.db"
CAMINHO_DB = str(caminho_absoluto)
def criar_banco():
    conn = sqlite3.connect(CAMINHO_DB)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS animal (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        identificacao TEXT NOT NULL,
        nome TEXT,
        data_nascimento TEXT,
        data_entrada TEXT,
        data_saida TEXT,
        sexo TEXT,
        status TEXT,
        raca_id INTEGER,
        lote_id INTEGER,
        mae_id INTEGER,
        pai_id INTEGER,
        origem TEXT,
        codigo_rfid TEXT,
        foto_url TEXT
    )
    """)
    
    conn.commit()
    conn.close()
    print("✅ Banco de dados atualizado com a estrutura profissional.")
