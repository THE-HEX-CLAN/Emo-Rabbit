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

@app.route('/Emotion')
def home():
    return render_template('Emotion.html')


@app.route("/",methods = ["GET","POST"])
def Index():
    return(render_template("EmoRabbit.html"))

@app.route("/get_summary",methods=["GET","POST"]) 
def get_summary():
    if req.method=="POST":
        # The token to the pretrained model
        API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        headers = {"Authorization": f"Bearer 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"}
