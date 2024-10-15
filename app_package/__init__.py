#importar librerias
from flask import Flask
import pymysql

#app config

app = Flask(__name__, template_folder='templates')    

def db_open():
    db = pymysql.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    db=app.config['MYSQL_DB']
    )
    
    return db

