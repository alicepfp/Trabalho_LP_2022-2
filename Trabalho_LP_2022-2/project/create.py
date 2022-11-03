import sqlite3


conn = sqlite3.connect('funcionario.db')

cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS FUNCIONARIO")

sql = '''CREATE TABLE FUNCIONARIO(NOME CHAR(100) NOT NULL, DATANASC CHAR(100) NOT NULL, CPF CHAR(100) NOT NULL, CTPS CHAR(100) NOT NULL, SETOR CHAR(100) NOT NULL, CARGO CHAR(100) NOT NULL, MATRICULA CHAR(100) NOT NULL)'''

cursor.execute(sql)

conn.commit()

conn.close()

print("tabela criada")
