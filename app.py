# from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def hello_world():
#     return 'Hello World!'
#
#
# if __name__ == '__main__':
#     app.run()
from time import sleep
from flask import Flask, render_template, jsonify, request
import datetime
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

now = datetime.datetime.now()
timeString = now.strftime("%Y-%m-%d %H:%M")
epoch = now

templateData = {
'title': 'HELLO!',
'time': epoch,
'eloszka': 666
}

@app.route('/', methods=['GET','POST']) 
def foo():
    global templateData

    if request.method == 'POST':
        postFunction()
    if request.method == 'GET':
        print(templateData)
        return render_template('table.html', **templateData)

    return render_template('table.html', **templateData)


# @app.route('')

def postFunction():
    global templateData
    data = request.get_json()
    try:
        print(data['name'])
        templateData["title"] = data['name']
        # return render_template('index.html', **templateData)
    except(Exception):
        print("Error")

def show_the_login_form():
    print("request post else")

if __name__ == '__main__':
    app.run(debug=True, port=7070, host='0.0.0.0')

def main():
    while(1):
        home()

# <h1>My Personal Website</h1>
#     <p>Hi, this is my personal website.</p>
#     <button type="button">Click Me!</button>
#     <button class="btn btn-hg btn-primary">
#         Boss Button
#     </button>
#     <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">


    # if request.method == 'POST':
    #     return do_the_login()
    # else:
    #     return show_the_login_form()
    # if flask.request.method == 'POST':
    #     username = flask.request.values.get('user') # Your form's
    #     password = flask.request.values.get('pass') # input names
    #     your_register_routine(username, password)
    # else:
    # # You probably don't have args at this route with GET
    # # method, but if you do, you can access them like so:
    #     yourarg = flask.request.args.get('argname')
    #     your_register_template_rendering(yourarg)
    # now = datetime.datetime.now()
    # timeString = now.strftime("%Y-%m-%d %H:%M")
    # epoch = now

    # templateData = {
    #     'title': 'HELLO!',
    #     'time': epoch
    # }
    # return render_template('index.html', **templateData)
    # return render_template('index.html', posts=posts)