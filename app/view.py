from app import app, db, app_celery
from flask import render_template, redirect, request
from forms import SiteForm
from models import *
import requests
import pickle
import datetime

nsqd = NSQD(app.config['NSQD_SERVER'])

@app.route('/')
def index():
    tasks = Tasks.query.all()
    return render_template('index.html', tasks=tasks)

@app.route('/results')
def results():
    results = Results.query.all()
    return render_template('results.html', results=results)


@app.route('/addsite', methods=['GET', 'POST'])
def addsite():
    site_form = SiteForm()
    if request.method == 'POST':
        if site_form.validate_on_submit():
            address = request.form.get('address')
            task = Tasks(address=address, task_status='NOT_STARTED', timestamp=datetime.datetime.now())
            db.session.add(task)
            db.session.commit()
            check_site.delay(task.id)
            return redirect('/results')
    return render_template('add_site.html', form=site_form)

@app_celery.task()
def check_site(id):
    task = Tasks.query.get(id)
    task.task_status = 'PENDING'
    db.session.commit()
    address = task.address
    res = requests.get(address) 
    words_count=0
    if res.ok:
        words = res.text
        words_count = words.count('python')
            
    result = Results(address=address, words_count=words_count, http_status_code=res.status_code)
    pickled = pickle.dumps(result)
    nsqd.send("results", pickled)
    task.task_status = 'FINISHED'
    db.session.commit()
    