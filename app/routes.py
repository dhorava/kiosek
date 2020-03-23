from flask import render_template, flash, redirect, url_for
from app import app
from app.form import ForecastsForm
from app.databricks import DatabricksAPI

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'krabe'}
    return render_template('index.html', title='Home', user=user)

@app.route('/forecasty', methods=['GET', 'POST'])
def forecasty():

    form = ForecastsForm()
    db_api = DatabricksAPI()

    if form.validate_on_submit():
        email = form.email.data
        flash('Forecasty budou zaslány na email {}'.format(email))

        job_id = 4856
        db_api.runNow(job_id, email)

        return redirect(url_for('index'))

    return render_template('forecasty.html', title='Zaslat forecasty na email', form=form)


@app.route('/google10de6de442947866.html')
def googlewebmastertools():
    return render_template('google10de6de442947866.html')
