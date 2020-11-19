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

# app = Flask(__name__)
# Bootstrap(app)
# server = app.server
# csrf = CSRFProtect(app)

# @app.route('/', methods=['GET'])
# def dropdown():
#     songs = ['one', 'two', 'three', 'four']
      
#     #return 'This is where the main app page will appear'
#     return render_template('base.html', songs=songs)

# #data = pd.read_csv('/herokuspotify.csv')


# # @app.route('/predict', methods=['POST'])
# # def predict():
    
#     # prediction = render_10(chosen_song)

def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite3"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    DB = SQLAlchemy(app)
    app.config['SECRET_KEY'] = '<SECRET_KEY>'
    csrf = CSRFProtect(app)

    @app.route('/', methods=['GET'])
    def dropdown():
        
        #return 'This is where the main app page will appear'
        return render_template('base.html')

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

    return app
    
    
if __name__ == "__main__":
<<<<<<< HEAD
    app.run_server(debug=True)   
=======
    app.run_server(debug=True)   
>>>>>>> 9440031ee4a156e6c2a1d9b052d9dcbf1e848e11
