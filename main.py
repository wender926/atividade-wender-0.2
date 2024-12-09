from flask import Flask, render_template

app_Wender = Flask(__name__)


@app_Wender.route('/<id>')
def saudacoes(id):
    return render_template('homepage.html', nome=id)  


@app_Wender.route('/rota1')
def rota1():
    return 'Olá Usuário!!'

@app_Wender.route('/rota2')
def rota2():
    resposta = "<h3> Essa é uma página da rota 2 </h3>"
    return resposta


@app_Wender.route("/")
def homepage():
    return render_template("homepage.html")  

@app_Wender.route("/contato")
def contato():
    return render_template("contato.html")  


@app_Wender.route("/index")
def indice():
    return render_template("index.html")  

@app_Wender.route("/usuario")
def dados_usuario():
    nome_usuario = "Wender"  
    dados_usuario = {"profissao": "Aluno", "disciplina": "Banco de Dados"}
    return render_template("usuario.html", nome=nome_usuario, dados=dados_usuario) 


@app_Wender.route("/usuario/<nome_usuario>;<nome_profissao>;<nome_disciplina>")
def usuario(nome_usuario, nome_profissao, nome_disciplina):
    dados_usuario = {"profissao": nome_profissao, "disciplina": nome_disciplina}
    return render_template("usuario.html", nome=nome_usuario, dados=dados_usuario)  


if __name__ == "__main__":
    app_Wender.run(debug=True)  