from flask import Flask, render_template, request, redirect, url_for, flash
import ConecaoDB

app = Flask(__name__)
app.secret_key = 'mauanet'

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/login")
def login_aux():
    return render_template("login.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route('/autenticar', methods=['POST'])
def autenticar():
    email = request.form['email']
    senha = request.form['senha']
    senha2 = ConecaoDB.conexaoDB_Login(email)
    if(senha2==[]):
        return redirect(url_for('login'))
    else:
        resultado = ConecaoDB.conexaoDB_Login(email)
        senha2= resultado[0][0]
        if (senha == senha2):
            nome,ra,gtl = pegar_dados(email)
            return redirect(url_for('mostrar_nome', email=email, nome=nome, ra=ra, gtl=gtl))
        else:
            flash('Email ou senha incorreto')
    return redirect(url_for('login')) 
    
@app.route('/mostrar_nome/<email>/<nome>/<ra>/<gtl>')
def mostrar_nome(email,nome,ra,gtl):
    return render_template('home.html', email=email, nome=nome, ra=ra, gtl=gtl)

@app.route('/processar', methods=['POST'])
def processar():
    nome = request.form['nome']
    return redirect(url_for('mostrar_nome', nome=nome))

@app.route('/pegar_dados')
def pegar_dados(email):
    resul = ConecaoDB.conexaoDB_Dados(email)
    nome = resul[0][0]
    Ra = resul[0][1]
    resul2 = ConecaoDB.conexaoDB_DadosRa(Ra)
    gtl = resul2[0][0] + resul2[0][1] + resul2[0][2]
    return nome,Ra,gtl

@app.route('/boletim')
def boletim():
    return render_template('boletim.html')

app.run(debug=True)