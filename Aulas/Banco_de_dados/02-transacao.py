import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent
conexao = sqlite3.connect(ROOT_PATH / "meu_banco.sqlite")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

try:
    cursor.execute("INSERTO INTO clientes (nome, email) VALUES (?, ?)", ("Larry Amaral", "larryreis@gmail.com"))
    conexao.commit()
    
except Exception as exc:
    print(f"Ocorreu um erro!\nERRO: {exc}")
    conexao.rollback()
