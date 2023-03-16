from flask import Flask, flash
from flask import request
from flask import Flask, render_template, url_for
from flask import request as req            #req is used for communication between the front end and the back end
import requests
#from flask_sqlalchemy import SQLAlchemy
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__,static_url_path="/static/css/GUI3.css")

model = joblib.load('sentiment-analysis.joblib')
vectorizer = joblib.load('vectorizer.joblib')
