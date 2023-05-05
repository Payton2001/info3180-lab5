from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = 'Som3$ec5etK*y'
db = SQLAlchemy(app)
# Instantiate Flask-Migrate library here
migrate = Migrate(app, db)
csrf = CSRFProtect(app)

from app import views