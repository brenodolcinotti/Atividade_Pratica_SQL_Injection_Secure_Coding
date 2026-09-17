from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from werkzeug.security import check_password_hash

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    erro = None
    if request.method == 'POST':
        usuario = request.form['username']
        senha = request.form['password']
        
        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()
        
        # ETAPA 10 e 14: Consulta PARAMETRIZADA (Secure Coding)
        # Busca apenas pelo usuário e deixa a senha para o Werkzeug validar
        sql = "SELECT * FROM usuarios WHERE username = ?"
        print(f"\n[SEGURO] Consulta parametrizada buscando usuário: {usuario}")
        
        cursor.execute(sql, (usuario,))
        user = cursor.fetchone()
        conn.close()
        
        # ETAPA 14: Verifica se o usuário existe E se o hash da senha confere
        if user and check_password_hash(user[2], senha):
            return redirect(url_for('painel', username=user[1]))
        else:
            erro = "Acesso negado. Usuário ou senha incorretos."
            
    return render_template('login.html', erro=erro)

@app.route('/painel/<username>')
def painel(username):
    return render_template('painel.html', username=username)

if __name__ == '__main__':
    print("Iniciando servidor SEGURO na porta 5001...")
    app.run(debug=True, port=5001)