from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class ForecastsForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Potvrdit')
