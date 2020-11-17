from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap




app = Flask(__name__)
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite3"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
DB = SQLAlchemy(app)

#return app

@app.route('/', methods=['GET'])
def dropdown():
    songs = ['one', 'two', 'three', 'four']
    #return 'This is where the main app page will appear'
    return render_template('base.html', songs=songs)



@app.route('/predict')
def results():
    return render_template('BS.html', title='Predict and Listen')
    
    
if __name__ == "__main__":
    app.run(debug=True)   