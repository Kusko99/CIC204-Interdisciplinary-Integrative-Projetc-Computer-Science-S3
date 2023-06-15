from flask import Flask, render_template, request, redirect, url_for, flash,session
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

@app.route("/home2")
def home2():
    email = session.get('email')
    nome = session.get('nome')
    ra = session.get('ra')
    gtl = session.get('gtl')
    return redirect(url_for('mostrar_nome', email=email, nome=nome, ra=ra, gtl=gtl))

@app.route("/mapa")
def mapa():
    return render_template("mapa.html")

@app.route("/boletim")
def boletim():
    email = session.get('email')
    nome = session.get('nome')
    ra = session.get('ra')
    gtl = session.get('gtl')
    return redirect(url_for('mostrar_nome2', email=email, nome=nome, ra=ra, gtl=gtl))

@app.route("/horarios")
def horarios():
    email = session.get('email')
    nome = session.get('nome')
    ra = session.get('ra')
    gtl = session.get('gtl')
    return redirect(url_for('mostrar_nome3', email=email, nome=nome, ra=ra, gtl=gtl))

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
    session['email'] = email
    session['nome'] = nome
    session['ra'] = ra
    session['gtl'] = gtl
    return render_template('home.html', email=email, nome=nome, ra=ra, gtl=gtl)

@app.route('/mostrar_nome2/<email>/<nome>/<ra>/<gtl>')
def mostrar_nome2(email,nome,ra,gtl):
    return render_template('boletim.html', email=email, nome=nome, ra=ra, gtl=gtl)

@app.route('/mostrar_nome3/<email>/<nome>/<ra>/<gtl>')
def mostrar_nome3(email,nome,ra,gtl):
    return render_template('horarios.html', email=email, nome=nome, ra=ra, gtl=gtl)

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

app.run(debug=True)