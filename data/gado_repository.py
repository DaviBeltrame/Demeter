import os
import sqlite3
from pathlib import Path

# Converter para caminho UNC (evita problemas com acentos)
caminho_absoluto = Path.home() / "Documents" / "IA" / "Demeter" / "data" / "gado.db"
CAMINHO_DB = str(caminho_absoluto)
def criar_banco_gado():
    conn = sqlite3.connect(CAMINHO_DB)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS gado (
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
    # 🧬 Evento de saúde
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS evento_saude (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        animal_id INTEGER,
        diagnostico TEXT,
        tratamento TEXT,
        proxima_avaliacao TEXT,
        FOREIGN KEY (animal_id) REFERENCES animal(id)
    )
    """)

    # 💉 Vacina
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS vacina (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        laboratorio TEXT,
        intervalo_meses INTEGER
    )
    """)

    # 🔗 Relacionamento evento-vacina
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS evento_vacina (
        evento_id INTEGER,
        vacina_id INTEGER,
        PRIMARY KEY (evento_id, vacina_id),
        FOREIGN KEY (evento_id) REFERENCES evento_saude(id),
        FOREIGN KEY (vacina_id) REFERENCES vacina(id)
    )
    """)
    
    conn.commit()
    conn.close()
    print("✅ Banco de dados atualizado com a estrutura profissional.")
