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

#backend that connects Emotion detection page 
@app.route('/Emotion')
def home():
    return render_template('Emotion.html')

#decorator that directs the user to view the sentiment after clicking the button
@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['text']
    text = vectorizer.transform([text])
    prediction = model.predict(text)[0]
    return render_template('Emotion.html', prediction=prediction)

@app.route("/SignUp")
def SignUp():
    if request.method == 'POST':
        if not request.form['firstName'] or not request.form['lastName'] or not request.form['email'] or not request.form['password']:
            flash('Please enter all the fields','error')
        else:
           signUp = SignUp(request.form['name'], request.form['city'],
            request.form['addr'], request.form['pin']) 
          
           flash('Record was successfully added')   
    return(render_template("signup.html"))

@app.route("/AboutUs")
def AboutUs():
    return(render_template("AboutUs.html"))

@app.route("/get_summary",methods=["GET","POST"]) 
def get_summary():
    if req.method=="POST":
        input_text = request.form["input_text"]
        # The token to the pretrained model
        API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        headers = {"Authorization": f"Bearer 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"}

#send the query to the model and get the response
        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()
        
#load the query using the input text, minimum and maximum lengths of the summary
        output = query({
            "inputs": input_text,
            "parameters": {"min_length" : min_len, "max_length" : max_len},
        })[0]
        #return the summarized output 
        #use the variable names 'result' as given in the front end
        return render_template("GUI3.html", result = output["summary_text"]) 
    else:
        return(render_template("GUI3.html"))  
if __name__ == '__main__':
   # db.create_all()
    app.debug = True #should be true for testing, should be false for production
    app.run()          
