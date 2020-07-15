
from gevent import monkey
from gevent.event import Event
# from gevent_tasks import TaskManager
import gevent
monkey.patch_all()

from apscheduler.schedulers.gevent import GeventScheduler
from apscheduler import events
from flask import Flask, render_template, jsonify, request

import os
import datetime
from datetime import datetime
from time import sleep
import time

import pdfkit
import main2

app = Flask(__name__)

# ---------------------------- HOW TO USE -------------------

# - wysłać postmanem json: 
# {
# 	"name": "aqwesvsdgweg"
# }

# - nacisnąć http Get 
# - uaktualnia się item1

posts = [
    {
        'author': 'cefwefw',
        'title': 'eloszka',
        'content': 'werwer',
        'date_posted': 'April 21, 2018'
    },
    {
        'author': 'cefadfbwefw',
        'title': 'eloszafbdfka',
        'content': 'wSDFerwer',
        'date_posted': 'April 13, 2018'
    }
]

now = datetime.now()
timeString = now.strftime("%Y-%m-%d %H:%M")
epoch = now

templateData = {
'OZN_WE_POM': 'TE1',
'OZN_WE_POM_DESC' : 'temperatura odpływu',
'NR_TORU': 1,
'RODZ_CZUJ': 'Pt100',
'TYP_CZUJ': 'TOPE412',
'PROD': 'producent',
'ZAKR_POM': '0…150°C',
'WYM_DOK': '±1°C',
'WZ_INFO': 'Piec kalibracyjny DBC 150 TS, nr fabr. 10349',

'WZPRK_1': 0,
'WOPRK_1': 0,
'OPRK_1' : 0,
'KOR_1'  : 0,
'WZPK_1' : 0,
'WOPK_1' : 0,
'OPK_1'  : 0,

'WZPRK_2': 2,
'WOPRK_2': 2,
'OPRK_2' : 2,
'KOR_2'  : 2,
'WZPK_2' : 2,
'WOPK_2' : 2,
'OPK_2'  : 2,

'WZPRK_3': 3,
'WOPRK_3': 3,
'OPRK_3' : 3,
'KOR_3'  : 3,
'WZPK_3' : 3,
'WOPK_3' : 3,
'OPK_3'  : 3
}

def webapp_run():
    print('Webapp working.')
    app.run(debug=False, port=7070, host='0.0.0.0')

@app.route('/', methods=['GET','POST']) 
def home():
    global templateData

    if request.method == 'POST':
        postFunction()
    if request.method == 'GET':
        print(templateData)
        render_template('index.html', **templateData)
    return render_template('index.html', **templateData)

@app.route('/table')
def table():
    return render_template('table.html', **templateData)

def postFunction():
    global templateData
    data = request.get_json()
    try:
        print(data['name'])
        templateData["title"] = data['name']
        # return render_template('index.html', **templateData)
    except(Exception):
        print("Error")

def doPdf():
    print('doPdf start')
    try:
        info = pdfkit.from_url('http://localhost:7070/table', 'tableOut.pdf')
        if (info):
            print('merging pdfs...')
            main2.merge4()
        print('Info: ', info)
    except(Exception):
        print('Cannot open url or sth.')

def tick():
    print('Tick! The time is: %s' % datetime.now())


scheduler = GeventScheduler()

if __name__ == '__main__':
    scheduler.add_job(webapp_run)
    # scheduler.add_job(doPdf, 'interval', seconds=15)
    # scheduler.add_job(tick, 'interval', seconds=4)

    g = scheduler.start() 
    try:
        g.join()
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()

