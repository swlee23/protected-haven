from flask import Flask, render_template, redirect
from models import connect_db, Lang

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///protected_haven'
app.config['SQLALCHEMY-TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

from flask_debugtoolbar import DebugToolbarExtension
app.config['SECRET_KEY'] = 'whateveryouwant'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

@app.route('/')
def home():
    langs = Lang.query.all()


    return render_template('index.html', langs=langs)

@app.route('/action/<lang>')
def action(lang): 
    return

@app.route('/report/<lang>')
def report(lang):
    lang = Lang.query.get_or_404(lang)

    return render_template('report.html', lang=lang)

@app.route('/confirmation/<lang>')
def confirmation(lang): 
    return

@app.route('/error/<lang>')
def error(lang):
    return

@app.route('/admin')
def admin():
    return