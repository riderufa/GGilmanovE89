from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_celery import make_celery
# from sites import blueprint

app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)
app.config.update(
    CELERY_IMPORTS = ['app', 'view']
)

app_celery = make_celery(app)

import models
db.create_all()
