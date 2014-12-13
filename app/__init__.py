import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)

print "CHECK ENVIRON APP SETTINGS: ", os.environ['APP_SETTINGS']

app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

from app import views
from app import models

# check environment config

print os.environ['DATABASE_URL']
