#import de bibliotecas, arquivos e funções
from flask_login import UserMixin
from . import db

#criação da classe usuario que da origem a tabela usuario no banco de dados 
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) #primary key para o sqlalchemy
    user = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    regnum = db.Column(db.String(1000))
