from flask import Flask, render_template, redirect, url_for, request, session
import DbConnect
import Main_mmedias

app = Flask(__name__)
app.secret_key = 'mauanet'

@app.route('/')
def standard():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    ra = '19.00468-0'
    gtl = DbConnect.get_GTL_aluno(ra)
    id_materias = DbConnect.get_GTL_id_Materias(gtl)
    materias = DbConnect.get_nome_id_materias(id_materias)
    return render_template('menu.html', materias=materias)

@app.route("/info_materia/<nome_materia>")
def info_materia(nome_materia):
    id_materia = DbConnect.get_id_materia_nome(nome_materia)
    peso_prova = DbConnect.get_peso_prova(id_materia)
    peso_trabalho = DbConnect.get_peso_trabalho(id_materia)
    quantidade_prova = DbConnect.get_quantidade_prova(id_materia)
    quantidade_trabalho = DbConnect.get_quantidade_trabalho(id_materia)
    session['quantidade_prova'] = quantidade_prova
    session['quantidade_trabalho'] = quantidade_trabalho
    return render_template('materia.html', nome_materia=nome_materia, peso_prova=peso_prova, peso_trabalho=peso_trabalho, quantidade_trabalho=quantidade_trabalho, quantidade_prova=quantidade_prova)

@app.route("/minimo_esforco,<nome_materia>,<peso_prova>,<peso_trabalho>", methods=["GET", "POST"])
def minimo_esforco(nome_materia,peso_prova,peso_trabalho):  
    quantidade_prova = session.get('quantidade_prova')
    quantidade_trabalho = session.get('quantidade_trabalho')
    if request.method == 'POST':
        psub = request.form.get("psub")
        inputs_prova = []
        inputs_trabalho = []
        for i in range(quantidade_prova):
            input_prova = request.form.get("input_prova{}".format(i))
            print(input_prova)
            inputs_prova.append(input_prova)
        for i in range(quantidade_trabalho):
            input_trabalho = request.form.get("input_trabalho{}".format(i))
            print(input_trabalho)
            inputs_trabalho.append(input_trabalho)
        
        theodoro_senpai = Main_mmedias.CalcME(inputs_prova,inputs_trabalho,quantidade_prova,quantidade_trabalho,psub,peso_prova,peso_trabalho)
        print(theodoro_senpai)
        # p1 = theodoro_senpai.P1
        # p2 = theodoro_senpai.P2
        # psub == -1
        # if psub == 'com_psub' :
        #     psub = theodoro_senpai.Psub
        # trabalhos = []
        # for i in range(quantidade_trabalho):
        #     pre_string = 'T'  + str(i+1)
        #     trabalhos.append(theodoro_senpai.pre_string)

        # print(p1)
        # print(p2)
        # print(psub)
        # print(trabalhos)
        # print("Psub:", psub)
        # print("Inputs Prova:", inputs_prova)
        # print("Inputs Trabalho:", inputs_trabalho)
    return "Deu certo meu pau na sua mão!!!!"
@app.route("/resultados,<nome_materia>,<quantidade_prova>,<quantidade_trabalho>,<theodoro_senpai>,<psub>")
def resultados(nome_materia,quantidade_prova,quantidade_trabalho,theodoro_senpai,psub):
    p1 = theodoro_senpai.P1
    p2 = theodoro_senpai.P2
    psub == -1
    if psub == 'com_psub' :
        psub = theodoro_senpai.Psub
    trabalhos = []
    for i in range(quantidade_trabalho):
        pre_string = 'T'  + str(i+1)
        trabalhos.append(theodoro_senpai.pre_string)

    print(p1)
    print(p2)
    print(trabalhos)
    if psub != -1:
        print(psub)
    

if __name__ == '__main__':
    app.run(debug=True)
