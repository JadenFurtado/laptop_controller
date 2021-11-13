from flask import Flask, session
from flaskext.mysql import MySQL
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

app.config['DEBUG']=True
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'ppt_controller'

from app import views
from app import user_views
from app import login_view
from app import house_view
from app import slide_show