import os
import datetime

from flask import render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
from azure.storage.blob import BlockBlobService

from app import app
from app.form import ForecastsForm
from app.upload_form import MonetaForm, CreditasForm
from app.databricks import DatabricksAPI


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'krabe'}
    return render_template('index.html', title='Domů', user=user)


@app.route('/forecasty', methods=['GET', 'POST'])
def forecasty():

    account = "redmediadwh"   # Azure account name
    key = "ePYDdZb74+ZxX1Ij/Ue+nMyMGQePX8fXVyxsllcR3OtEoYneLmnzjAOQC4sxonFCtLhDT3VyCZ9mDhxSQ7aWzw=="      # Azure Storage account access key
    container = "kiosek" # Container name

    blob_service = BlockBlobService(account_name=account, account_key=key)

    form = ForecastsForm()
    db_api = DatabricksAPI()

    job_id = 4857
    table = db_api.getJobRuns(job_id)

    #print(table)

    for run in table["runs"]:
        if(run["state"]["life_cycle_state"] == "RUNNING" or run["state"]["life_cycle_state"] == "PENDING"):
            pass
        elif(run["state"]["result_state"] == "SUCCESS"):
            local_filename = os.path.join("app/static/downloads/forecasty/", "forecasty-" + str(run["run_id"]) + ".csv")
            if os.path.isfile(local_filename):
                #print("exists")
                pass
            else:
                try:
                    b = blob_service.get_blob_to_bytes(container, "forecasty/forecasty-" + str(run["run_id"]) + ".csv")

                    fp = open(local_filename, "ab")
                    fp.write(b.content)
                    fp.flush()
                    fp.close()
                except Exception as e:
                    print(str(e))
                    pass

    if form.validate_on_submit():
        email = form.email.data
        flash('Forecasty budou zaslány na {}'.format(email))

        db_api.runNow(job_id, email)

        return redirect(url_for('forecasty'))

    return render_template('forecasty.html', title='Forecasty', form=form, table=table)


@app.route('/moneta', methods=['GET', 'POST'])
def moneta():

    form = MonetaForm()
    db_api = DatabricksAPI()

    job_id = 4890
    table = db_api.getJobRuns(job_id)

    if form.validate_on_submit():
        file = request.files['file']

        if 'file' not in request.files:
            flash('Nebyl vybrán soubor!')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            account = "redmediadwh"   # Azure account name
            key = "ePYDdZb74+ZxX1Ij/Ue+nMyMGQePX8fXVyxsllcR3OtEoYneLmnzjAOQC4sxonFCtLhDT3VyCZ9mDhxSQ7aWzw=="      # Azure Storage account access key
            container = "clients" # Container name

            blob_service = BlockBlobService(account_name=account, account_key=key)
            blob_service.create_blob_from_path(container, "moneta/"+filename, filepath)

            email = form.email.data

            flash('Report je právě aktualizován. Výsledek uvidíš níže v tabulce, informace o úspěšné atkualizaci ti přijde na {}'.format(email))

            db_api.runNow(job_id, email)

            return redirect(url_for('moneta'))

        return redirect(url_for('moneta'))

    return render_template('reporty.html', title='Moneta', form=form, table=table)


@app.route('/creditas', methods=['GET', 'POST'])
def creditas():

    form = CreditasForm()
    db_api = DatabricksAPI()

    job_id = 4926
    table = db_api.getJobRuns(job_id)

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
            blob_service.create_blob_from_stream(container, "creditas/"+filename, file)

            flash('Report je právě aktualizován, informace o dokončení ti přijde na {}'.format(form.email.data))
            return redirect(url_for('creditas'))

        return redirect(url_for('creditas'))

    return render_template('reporty.html', title='Creditas', form=form, table=table)


@app.route('/google10de6de442947866.html')
def googlewebmastertools():
    return render_template('google10de6de442947866.html')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


def format_datetime(value, format="full"):
    if format == "full":
        format = "%d.%m.%Y %H:%M:%S"
    elif format == "medium":
        format = "%H:%M:%S"
    elif format == "min":
        format = "%M:%S"
    return datetime.datetime.fromtimestamp(value/1000.0).strftime(format)

app.jinja_env.filters['datetime'] = format_datetime
