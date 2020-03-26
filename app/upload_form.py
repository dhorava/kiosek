from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class MonetaForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    file = FileField('Pozor - název souboru musí začínat na "powerbi_leads"! Například tedy "powerbi_leads_25-03-2020.xlsx". V opačném případě skript neproběhne.', validators=[FileRequired()])
    submit = SubmitField('Potvrdit')

class CreditasForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    file = FileField('Excel', validators=[FileRequired()])
    submit = SubmitField('Potvrdit')
