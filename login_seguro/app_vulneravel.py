from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    erro = None
    if request.method == 'POST':
        usuario = request.form['username']
        senha = request.form['password']
        
        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()
        
        # ETAPA 4: Implementação VULNERÁVEL com concatenação direta de strings
        sql = "SELECT * FROM usuarios WHERE username = '" + usuario + "' AND password = '" + senha + "'"
        print("\n[ALERTA] Consulta executada:", sql)
        
        try:
            cursor.execute(sql)
            user = cursor.fetchone()
        except Exception as e:
            print("Erro no banco:", e)
            user = None
            
        conn.close()
        
        if user:
            return redirect(url_for('painel', username=user[1]))
        else:
            erro = "Acesso negado. Usuário ou senha incorretos."
            
    return render_template('login.html', erro=erro)

@app.route('/painel/<username>')
def painel(username):
    return render_template('painel.html', username=username)

if __name__ == '__main__':
    print("Iniciando servidor VULNERÁVEL na porta 5000...")
    app.run(debug=True, port=5000)