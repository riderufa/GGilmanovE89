from flask_wtf import FlaskForm
from wtforms import StringField

class SiteForm(FlaskForm):
    address = StringField('address')