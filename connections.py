import os

import flask_login
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine


def get_env_variable(name):
    try:
        return os.environ[name]
    except KeyError:
        message = "Expected environment variable '{}' not set.".format(name)
        raise Exception(message)


# If you are using SQLite:
DB_URL = 'sqlite:///database.sqlite3'

ENGINE = create_engine(DB_URL).raw_connection()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
DB = SQLAlchemy(app)

# If you are using Postgres:
"""
POSTGRES_DB = "DB_NAME"
POSTGRES_URL = "IP:PORT"
POSTGRES_USER = get_env_variable("POSTGRES_USER")
POSTGRES_PW = get_env_variable("POSTGRES_PW")

DB_URL = (
    f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PW}@{POSTGRES_URL}/{POSTGRES_DB}"
)
ENGINE = create_engine(DB_URL)

app = Flask(__name__)
app.secret_key = "secretkey"
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
DB = SQLAlchemy(app)"""

login_manager = flask_login.LoginManager()
login_manager.init_app(app)
