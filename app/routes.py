from flask import render_template
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
        flash('Forecasty budou zaslány na email {}'.format(form.username.email))

        email = form.username.email
        job_id = 4856
        db_api.runNow(job_id, email)

        return redirect('/index')

    return render_template('forecasty.html', title='Zaslat forecasty na email', form=form)
