from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from forms import RegistrationForm, LoginForm
from flask_wtf.csrf import CSRFProtect
from os import getenv
from joblib import load

app = Flask(__name__)
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite3"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
DB = SQLAlchemy(app)
app.config['SECRET_KEY'] = '<SECRET_KEY>'
csrf = CSRFProtect(app)
#return app

@app.route('/', methods=['GET'])
def dropdown():
    songs = ['one', 'two', 'three', 'four']
        # <html lang="en">
        # <head>
        # <meta charset="UTF-8">
        # <title>Dropdown</title>
        # </head>
        # <body>
        # <select name= Songs method="GET" action="/">
        # {% for song in songs%}
        # <option value= "{{song}}" SELECTED>{{song}}</option>"
        # {% endfor %}
        # </select>
        # </select>
        # </body>
        # </html>
    #return 'This is where the main app page will appear'
    return render_template('base.html', songs=songs)



@app.route('/predict')
def results():
    return render_template('BS.html', title='Predict and Listen')

@app.route('/about')
def about():
    return render_template('about.html', title='Spotify Pick Me - About')


@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

@app.route('/process')
def process():
    return render_template('process.html', title='Our Process in Creating Predictify')


    
    
if __name__ == "__main__":
    app.run(debug=True)   