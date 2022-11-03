import sqlite3

def create_funcionario(registro):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    conn = sqlite3.connect('/home/alice/Documentos/Trabalho_LP_2022-2/Trabalho_LP_2022-2/project/funcionario.db', check_same_thread=False)
    cursor = conn.cursor()
    sql = "INSERT INTO FUNCIONARIO (NOME, DATANASC, CPF, CTPS, SETOR, CARGO, MATRICULA) VALUES(?,?,?,?,?,?,?)"
    cur = conn.cursor()
    cur.execute(sql, registro)
    conn.commit()
    return
