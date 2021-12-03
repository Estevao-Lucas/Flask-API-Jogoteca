import os

SECRET_KEY = 'estevao'
# Configs do MySQL
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'Tevit*098'
MYSQL_DB = 'jogoteca'
MYSQL_PORT = 3306
#direciona para que pasta vai o arquivo
UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) \
    + '/uploads' #__file__ tem o valor da raiz do projeto jogoteca.py
