import sqlite3
from werkzeug.security import generate_password_hash

def init_db():
    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()
    
    # Cria a tabela de usuários
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    
    # Limpa a tabela para evitar duplicações ao rodar o script novamente
    cursor.execute('DELETE FROM usuarios')
    
    # USUÁRIO 1: Vulnerável (Senha em texto puro para a Etapa 4)
    cursor.execute("INSERT INTO usuarios (username, password) VALUES ('admin', 'admin123')")
    
    # USUÁRIO 2: Seguro (Senha com Hashing para a Etapa 13)
    hash_aluno = generate_password_hash('aluno123')
    cursor.execute("INSERT INTO usuarios (username, password) VALUES (?, ?)", ('aluno', hash_aluno))
    
    conn.commit()
    conn.close()
    print("Banco de dados 'banco.db' gerado com sucesso!")
    print("-> Usuário 'admin' criado com senha em texto puro (admin123).")
    print("-> Usuário 'aluno' criado com senha criptografada (aluno123).")

if __name__ == '__main__':
    init_db()