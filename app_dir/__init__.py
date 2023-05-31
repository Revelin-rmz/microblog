from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

"""
keep this import below cause fucking hell the flask db init wont work otherwise,
see jwmuray @ https://github.com/miguelgrinberg/microblog/issues/69
ignore the tutorial
"""
from config import Config           # nopep8

app = Flask(__name__)


app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app_dir import routes, models  # nopep8
