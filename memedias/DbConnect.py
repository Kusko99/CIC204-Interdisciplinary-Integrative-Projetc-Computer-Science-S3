from mysql.connector import connection


host ='localhost'
user ='user'
password = 'password'
database = 'db_MauaNet'

def get_GTL_aluno(ra):
    db_connection = connection.MySQLConnection(host=host, user = user, password = password, database=database)
    cursor = db_connection.cursor()

    query = "SELECT GTL FROM GTL WHERE Ra = (%s)"
    values = (ra,)
    cursor.execute(query,values)
    resultados = cursor.fetchall()

    cursor.close()
    db_connection.commit()
    db_connection.close()

    return resultados[0][0]

def get_GTL_id_Materias(gtl):
    db_connection = connection.MySQLConnection(host=host, user = user, password = password, database=database)
    cursor = db_connection.cursor()

    query = "SELECT DISTINCT Id_Materia FROM Aula WHERE GTL = (%s) ORDER BY Id_Materia; "
    values = (gtl,)
    cursor.execute(query,values)
    resultados = cursor.fetchall()

    cursor.close()
    db_connection.commit()
    db_connection.close()

    id_materias = []

    for resultado in resultados:
        id_materias.append(resultado[0])

    return id_materias

def get_nome_id_materias(lista_ids):
    #Deve se entrar com uma lista contendo os ids
    lista_nomes = []

    for id in lista_ids:
        db_connection = connection.MySQLConnection(host=host, user = user, password = password, database=database)
        cursor = db_connection.cursor()

        query = "SELECT nome FROM Materia WHERE Id_Materia = (%s)"
        values = (id,)
        cursor.execute(query,values)
        resultado = cursor.fetchall()

        cursor.close()
        db_connection.commit()
        db_connection.close()

        lista_nomes.append(resultado[0][0])

    return lista_nomes

def get_peso_prova(id_materia):
    db_connection = connection.MySQLConnection(host=host, user=user, password=password,database=database)
    cursor = db_connection.cursor()

    query = "SELECT Peso_Prova FROM Materia WHERE Id_Materia = (%s)"
    values = (id_materia,)
    cursor.execute(query,values)
    resultado = cursor.fetchall()

    cursor.close()
    db_connection.commit()
    db_connection.close()

    return resultado[0][0]

def get_peso_trabalho(id_materia):
    db_connection = connection.MySQLConnection(host=host, user=user, password=password,database=database)
    cursor = db_connection.cursor()

    query = "SELECT Peso_Trabalho FROM Materia WHERE Id_Materia = (%s)"
    values = (id_materia,)
    cursor.execute(query,values)
    resultado = cursor.fetchall()

    cursor.close()
    db_connection.commit()
    db_connection.close()

    return resultado[0][0]


def get_quantidade_prova(id_materia):
    db_connection = connection.MySQLConnection(host=host, user=user, password=password,database=database)
    cursor = db_connection.cursor()

    query = "SELECT Quantidade_Prova FROM Materia WHERE Id_Materia = (%s)"
    values = (id_materia,)
    cursor.execute(query,values)
    resultado = cursor.fetchall()

    cursor.close()
    db_connection.commit()
    db_connection.close()

    return resultado[0][0]

def get_quantidade_trabalho(id_materia):
    db_connection = connection.MySQLConnection(host=host, user=user, password=password,database=database)
    cursor = db_connection.cursor()

    query = "SELECT Quantidade_Trabalho FROM Materia WHERE Id_Materia = (%s)"
    values = (id_materia,)
    cursor.execute(query,values)
    resultado = cursor.fetchall()

    cursor.close()
    db_connection.commit()
    db_connection.close()

    return resultado[0][0]

def get_id_materia_nome(nome_materia):
    db_connection = connection.MySQLConnection(host=host, user=user, password=password,database=database)
    cursor = db_connection.cursor()

    query = "SELECT Id_Materia FROM Materia WHERE Nome  = (%s)"
    values = (nome_materia,)
    cursor.execute(query,values)
    resultado = cursor.fetchall()

    cursor.close()
    db_connection.commit()
    db_connection.close()

    return resultado[0][0]
