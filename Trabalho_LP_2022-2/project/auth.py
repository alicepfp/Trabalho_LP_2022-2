#import de bibliotecas, arquivos e funções
from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from .models import User
from . import db

auth = Blueprint('auth', __name__)

#rota de login da aplicação
@auth.route('/login')
def login():
    return render_template('login.html')

#funcionamento do login
@auth.route('/login', methods=['POST'])
def login_post():
    print ("entrou no login post")
    user = request.form.get('usuario')
    password = request.form.get('senha')
    print('formulario:', user)

    user2 = User.query.filter_by(user=user).first()
    print(user2)

    #checagem se o usuario existe
    #checa se a senha fornecida corresponde a do banco
    if not user2 or not check_password_hash(user2.password, password): 
        flash('Login incorreto, tente novamente.')
        return redirect(url_for('auth.login')) #caso usuario inexistente ou senha incorreta, reloga a pagina

    #caso o fornecido esteja correto, redirecionamento para pagina principal
    login_user(user2)
    return redirect(url_for('main.profile'))

#rota para a criação de login
@auth.route('/signup')
def signup():
    return render_template('register_user.html')

#funcionamento da criação de login
@auth.route('/signup', methods=['POST'])
def signup_post():

    user = request.form.get('Nome-usuario')
    regnum = request.form.get('Matricula-usuario')
    password = request.form.get('Senha')

    print("#######", user, regnum, password)
    user2 = User.query.filter_by(user=user).first() #checagem se ja existe esse usuario cadastrado no banco

    if user2: #caso o usuario já exista a pagina recarrega  
        flash('Usuário já existente')
        return redirect(url_for('auth.signup'))

    #criação de novo usuario com a senha em hash para salvar no banco
    new_user = User(user=user, regnum=regnum, password=generate_password_hash(password, method='sha256'))

    #adiciona o usuario ao banco
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))

