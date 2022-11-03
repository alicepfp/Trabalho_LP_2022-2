import sqlite3

conn = sqlite3.connect('/home/alice/Documentos/Trabalho_LP_2022-2/Teste_Trabalho/project/funcionario.db', check_same_thread=False )

def busca_funcionario(busca):
    cur = conn.cursor()
    sql = '''SELECT * FROM FUNCIONARIO WHERE NOME LIKE ?'''
    cur.execute(sql,['%'+busca+'%'])
    output = cur.fetchall()
    print(busca)
    for row in output:
        print(row)
    conn.commit()
    return output
