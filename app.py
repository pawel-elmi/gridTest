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
from flask import Flask, render_template, jsonify
import datetime
app = Flask(__name__)


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


@app.route('/')
def home():
    now = datetime.datetime.now()
    # timeString = now.strftime("%Y-%m-%d %H:%M")
    epoch = now

    templateData = {
        'title': 'HELLO!',
        'time': epoch
    }
    return render_template('index.html', **templateData)
    # return render_template('index.html', posts=posts)

# @app.route('')


if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')

def main():
    while(1):
        home()
        sleep(1)

# <h1>My Personal Website</h1>
#     <p>Hi, this is my personal website.</p>
#     <button type="button">Click Me!</button>
#     <button class="btn btn-hg btn-primary">
#         Boss Button
#     </button>
#     <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">