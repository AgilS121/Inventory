from flask import Flask
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = "flash message"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/inventory'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = True

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'inventory'

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'gilsatria121@gmail.com'
app.config['MAIL_PASSWORD'] = 'tojkwgmoynbokgmx'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)
mysql = MySQL(app)
db = SQLAlchemy(app)

from web import routes

