from email.mime import image
from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os

app_Wender = Flask(__name__)
app_Wender.secret_key = 'sua_chave_secreta'

# Arquivo JS
ARQUIVO_USUARIOS = 'usuarios.json'

def carregar_usuarios():
    if os.path.exists(ARQUIVO_USUARIOS):
        with open(ARQUIVO_USUARIOS, 'r') as arquivo:
            return json.load(arquivo)
    return []

def salvar_usuarios():
    with open(ARQUIVO_USUARIOS, 'w') as arquivo:
        json.dump(usuarios_cadastrados, arquivo, indent=4)

usuarios_cadastrados = carregar_usuarios()

@app_Wender.route('/')
def raiz():
    return render_template('index.html')

@app_Wender.route('/criar-conta', methods=['GET', 'POST'])
def criar_conta():
    if request.method == 'POST':
        dados_usuario = {
            'nome': request.form.get('nome'),
            'cpf': request.form.get('cpf'),
            'email': request.form.get('email'),
            'telefone': request.form.get('telefone'),
            'endereco': request.form.get('endereco'),
            'senha': request.form.get('senha')
        }
        confirmacao = request.form.get('confirmar_senha')
        
        if not all(dados_usuario.values()) or not confirmacao:
            flash('Preencha todos os campos!', 'error')
        elif dados_usuario['senha'] != confirmacao:
            flash('As senhas não coincidem!', 'error')
        elif not validar_senha(dados_usuario['senha']):
            flash('A senha não atende aos requisitos!', 'error')
        elif any(u['email'] == dados_usuario['email'] for u in usuarios_cadastrados):
            flash('Este email já está cadastrado!', 'error')
        else:
            usuarios_cadastrados.append(dados_usuario)
            salvar_usuarios() 
            flash('Cadastro realizado com sucesso!', 'success')
            return redirect(url_for('login'))

    return render_template('criar_conta.html')

@app_Wender.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('password')
        
        usuario = next((u for u in usuarios_cadastrados if u['email'] == email and u['senha'] == senha), None)
        
        if usuario:
            flash(f"Login realizado com sucesso! Bem-vindo, {usuario['nome']}!", 'success')
            return redirect(url_for('home', nome_usuario=usuario['nome']))
        else:
            flash('Email ou senha incorretos!', 'error')

    return render_template('login.html')

@app_Wender.route('/home')
def home():
    nome_usuario = request.args.get("nome_usuario", "Visitante")
    return render_template('home.html', nome_usuario=nome_usuario)

@app_Wender.route('/galeria')
def galeria():
    # Lista de imagens (substitua pelos nomes das suas imagens)
    return render_template('fotos.html', imagens=image)

def validar_senha(senha):
    import re
    pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{6,}$'
    return bool(re.match(pattern, senha))

if __name__ == '__main__':
    app_Wender.run()