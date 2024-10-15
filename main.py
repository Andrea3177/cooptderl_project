

from app_package import app
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from flask import redirect, url_for
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from flask_login import LoginManager

#run app
from app_package import views

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

app.secret_key = 'secret3mandarinas'
app.permanent_session_lifetime = timedelta(minutes=10)
app.testing = True


# Configuraci�n de base de datos

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Mandarina#33'
app.config['MYSQL_DB'] = 'cooptderl'

#conexion con base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Mandarina#33@localhost/cooptderl'

engine_coop = create_engine('mysql+pymysql://root:Mandarina#33@localhost/cooptderl', echo=True)

db = SQLAlchemy(app)

Session = sessionmaker(bind=engine_coop)
session = Session()

#config login manager
login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = 'login'  # Set the login view