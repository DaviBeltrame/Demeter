import os
import sys
from pathlib import Path
import sqlite3

# Configurar encoding para UTF-8
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

# Resolver problema do caminho com acentos
base_dir = Path.home() / "Documents" / "IA" / "Demeter"
os.chdir(base_dir)

# Caminho absoluto seguro para o banco de dados
DB_PATH = base_dir / "data" / "gado.db"

print(f"Diretório atual: {os.getcwd()}")
print(f"Caminho do banco: {DB_PATH}")

# Verificar/criar estrutura de pastas
(DB_PATH.parent).mkdir(parents=True, exist_ok=True)
print(f"Pasta do banco existe: {DB_PATH.parent.exists()}")

# Testar conexão com SQLite
try:
    conn = sqlite3.connect(str(DB_PATH))
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS teste (id INTEGER PRIMARY KEY, nome TEXT)")
    conn.commit()
    print("✅ Banco de dados criado com sucesso!")
    print(f"Tamanho do banco: {os.path.getsize(DB_PATH)} bytes")
except Exception as e:
    print(f"❌ Erro no banco de dados: {str(e)}")
finally:
    if conn:
        conn.close()

input("Pressione Enter para sair...")