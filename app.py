from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from forms import RegistrationForm, LoginForm
from flask_wtf.csrf import CSRFProtect
from os import getenv
import pandas as pd
from joblib import load
from predict import render_10
import csv
import sqlite3

app = Flask(__name__)
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite3"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
DB = SQLAlchemy(app)
app.config['SECRET_KEY'] = '<SECRET_KEY>'
csrf = CSRFProtect(app)
#conn = connect("sqlite:///spotify.db")
#curs = conn.cursor()
#with open('herokuspotify.csv', 'r') as Spotify_df:
#df = pandas.read_csv('herokuspotify.csv')
#df.to_sql(dataset, conn, if_exists='append', index=False)


#return app

@app.route('/', methods=['GET'])
def dropdown():
    songs = ['one', 'two', 'three', 'four']
      
    #return 'This is where the main app page will appear'
    return render_template('base.html', songs=songs)

#data = pd.read_csv('/herokuspotify.csv')


# @app.route('/predict', methods=['POST'])
# def predict():
    
    # prediction = render_10(chosen_song)

@app.route('/predict', methods=['GET', 'POST'])
def home():

    return render_10(request.values['song'])




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