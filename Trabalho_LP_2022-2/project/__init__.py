#import de bibliotecas, arquivos e funções
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager 

#inicialização do banco em sqlalchemy para os logins
db = SQLAlchemy()

#função para criar a aplicação flask
def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User
    
    #
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    #blueprint para as rotas do arquivo auth 
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    #blueprint para o arquivo main  
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
