# import de bibliotecas, arquivos e funções
from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from .insert import create_funcionario
from .search import busca_funcionario
from .alter import busca_altera_funcionario, altera_funcionario

main = Blueprint('main', __name__)

#rota para a tela inicial da aplicação com direcionamento de login
@main.route('/')
def index():
    return render_template('base.html')

#rota para a tela principal da aplicação (necessário estar logado para acessar)
@main.route('/profile')
@login_required
def profile():
    return render_template('index.html', user=current_user.user)

#rota para a ferramenta de busca de funcionários da aplicação
@main.route("/busca", methods =["GET",'POST'])
def buscar():
    if request.method == 'POST':
        if request.form['buscar'] == 'Buscar':
            return render_template("search.html")

#rota para a ferramenta de cadastro de funcionários da aplicação
@main.route("/cadastro", methods =['POST'])
def cadastro():
    if request.method == 'POST':
        if request.form['cadastrar-func'] == 'Cadastrar':
            return render_template("register.html")

#rora para a ferramenta de alteração do cadastro da aplicação
@main.route("/alterar", methods =['POST'])
def alterar():
    if request.method == 'POST':
        if request.form['alterar'] == 'Alterar Dados':
            return render_template("search_update.html")

#rota que realiza a busca de funcionarios dentro do banco de dados 
@main.route("/funcionario", methods = ["GET","POST"])
def funcionario():
    if request.method == 'POST':
        if request.form['buscar'] == 'Buscar':
            busca =request.form['employee_name']
            resultado = busca_funcionario(busca)
            return render_template("list.html", paragrafo = '''João da silva, 3735035/0060, 09809184727, 25/10/1989, Aquático, Assistente ADM, 122041900''')

#rota que realiza o cadastro de funcionarios no banco de dados 
@main.route("/registrado", methods = ["GET","POST"])
def cadastrado():
    nome = request.form.get('Nome')
    datanasc = request.form.get('Nascimento')
    cpf = request.form.get('CPF')
    ctps = request.form.get('CTPS')
    setor = request.form.get('Setor')
    cargo = request.form.get('Cargo')
    matricula = request.form.get('Matricula')
    print(nome, datanasc, cpf, ctps, setor, cargo, matricula, "usuario cadastrado")
    registro = [nome, datanasc, cpf, ctps, setor, cargo, matricula]
    create_funcionario(registro)    
    return render_template("registered.html")

#rota para a busca de funcionarios no banco de dados com fim de atualizar o cadastro (só aceita nomes específicos)    
@main.route("/searchupdate", methods = ["GET","POST"])
def search_update():
    if request.method == 'POST':
        if request.form['buscar'] == 'Buscar':
            buscaealtera =request.form['employee_name']
            global resultadoaltera
            resultadoaltera = busca_altera_funcionario(buscaealtera)
            return render_template("update.html", nome = resultadoaltera[0])

#rota para alterar os dados cadastrais de um funcionario no banco de dados
@main.route("/alterado", methods = ["GET","POST"])
def alterado():
    nome = request.form.get('Nome')
    datanasc = request.form.get('Nascimento')
    cpf = request.form.get('CPF')
    ctps = request.form.get('CTPS')
    setor = request.form.get('Setor')
    cargo = request.form.get('Cargo')
    matricula = request.form.get('Matricula')
    print(nome, datanasc, cpf, ctps, setor, cargo, matricula, "dados alterados")
    altera = [nome, datanasc, cpf, ctps, setor, cargo, matricula]
    altera.append(resultadoaltera[0])
    altera_funcionario(altera)    
    return render_template("updated.html")
