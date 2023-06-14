from mysql.connector import connection

host ='localhost'
user ='user'
password = 'password'
database = 'db_MauaNet'


def conexaoDB_Login(Email):

    db_connection = connection.MySQLConnection(host=host, user=user, password=password,database=database)
    cursor = db_connection.cursor()

    query = "SELECT Senha FROM Aluno_Boletim where Email = %s"
    values = [Email]
    cursor.execute(query,values)
    resultado = cursor.fetchall();
    
    cursor.close()
    db_connection.commit()
    db_connection.close()
    
    return(resultado)

def conexaoDB_Dados(Email):

    db_connection = connection.MySQLConnection(host=host, user=user, password=password,database=database)
    cursor = db_connection.cursor()

    query = "SELECT Nome,Ra FROM Aluno_Boletim where Email = %s"
    values = [Email]
    cursor.execute(query,values)
    resultado = cursor.fetchall();
    
    cursor.close()
    db_connection.commit()
    db_connection.close()
    
    return(resultado)

def conexaoDB_DadosRa(Ra):

    db_connection = connection.MySQLConnection(host=host, user=user, password=password,database=database)
    cursor = db_connection.cursor()
    
    query = "SELECT Grupo,Turma,Lab FROM GTL where Ra = %s"
    values = [Ra]
    cursor.execute(query,values)
    resultado = cursor.fetchall();
    
    cursor.close()
    db_connection.commit()
    db_connection.close()
    
    return(resultado)

def conexaoDB_Notas(Ra):

    db_connection = connection.MySQLConnection(host=host, user=user, password=password,database=database)
    cursor = db_connection.cursor()
    
    query = "SELECT valor FROM Nota where Ra = %s"
    values = [Ra]
    cursor.execute(query,values)
    resultado = cursor.fetchall();
    
    cursor.close()
    db_connection.commit()
    db_connection.close()
    
    return(resultado)
