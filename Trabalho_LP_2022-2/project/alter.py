import sqlite3 

conn =  conn = sqlite3.connect('/home/alice/Documentos/Trabalho_LP_2022-2/Trabalho_LP_2022-2/project/funcionario.db', check_same_thread=False )

def busca_altera_funcionario(buscaealtera):
    cur = conn.cursor()
    sql = '''SELECT * FROM FUNCIONARIO WHERE NOME = ?'''
    cur.execute(sql, [buscaealtera])
    output = cur.fetchone()
    print(buscaealtera)
    for row in output:
        print(row)
    conn.commit()
    return output

def altera_funcionario(altera):
    cur = conn.cursor()
    update = '''UPDATE FUNCIONARIO SET NOME=?, DATANASC=?, CPF=?, CTPS=?, SETOR=?, CARGO=?, MATRICULA=? WHERE NOME = ?'''
    cur.execute(update, altera)
    conn.commit()
    conn.close()
    return update
