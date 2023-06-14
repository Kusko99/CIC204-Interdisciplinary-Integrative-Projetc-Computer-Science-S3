from flask import Flask, render_template, redirect, url_for
import DbConnect

app = Flask(__name__)

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
    return render_template('materia.html', nome_materia=nome_materia)

if __name__ == '__main__':
    app.run(debug=True)

