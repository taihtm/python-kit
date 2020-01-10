import os
from flask import Flask
import sqlite3
from flask_pymongo import PyMongo
from flask_sqlalchemy import SQLAlchemy

from .config import config_by_name, basedir

db_mongo = PyMongo()
db_sql = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_by_name[config_name])
    db_mongo.init_app(app)
    db_sql.init_app(app)
    return app


def init_db_sqlite(app):
    # try:
    #     os.makedirs(app.instance_path)
    # except OSError:
    #     pass

    db = sqlite3.connect(
        os.path.join(basedir, 'user.db')
    )
    db.row_factory = sqlite3.Row

    with app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))
