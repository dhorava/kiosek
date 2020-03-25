import os

from flask import render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
from azure.storage.blob import BlockBlobService

from app import app
from app.form import ForecastsForm
from app.upload_form import MonetaForm
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

        job_id = 4857
        db_api.runNow(job_id, email)

        return redirect(url_for('index'))

    return render_template('forecasty.html', title='Zaslat forecasty na email', form=form)


@app.route('/moneta', methods=['GET', 'POST'])
def moneta():

    form = MonetaForm()
    db_api = DatabricksAPI()

    if form.validate_on_submit():
        file = request.files['file']

        if 'file' not in request.files:
            flash('Nebyl vybrán soubor!')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            account = "redmediadwh"   # Azure account name
            key = "ePYDdZb74+ZxX1Ij/Ue+nMyMGQePX8fXVyxsllcR3OtEoYneLmnzjAOQC4sxonFCtLhDT3VyCZ9mDhxSQ7aWzw=="      # Azure Storage account access key
            container = "clients" # Container name

            blob_service = BlockBlobService(account_name=account, account_key=key)
            blob_service.create_blob_from_stream(container, "moneta/"+filename, file)

            flash('Report je právě aktualizován, informace o dokončení ti přijde na {}'.format(form.email.data))
            return redirect(url_for('moneta'))

        return redirect(url_for('moneta'))

    return render_template('reporty.html', title='Aktualizovat Moneta report', form=form)


@app.route('/google10de6de442947866.html')
def googlewebmastertools():
    return render_template('google10de6de442947866.html')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']
