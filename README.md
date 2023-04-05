Hotel Review Summarization and Emotion Detection App

This is a web application that summarizes and detects the emotion of hotel reviews. The application uses Python Flask as the backend and the TfIdf algorithm for ML model training.

How to use

Clone the repository
Install dependencies with pip install -r requirements.txt.
Run the app with python app.py.
Navigate to http://localhost:5000 in your web browser.

Features

Enter any hotel review text and the app will summarize it and classify it as either positive, negative or neutral.
View a history of all past reviews and their classifications.
Access statistics on the most common emotions detected in the reviews.

How it works

The application uses a machine learning model trained on the TfIdf algorithm to detect the emotion of hotel reviews. The model is hosted on the backend and is accessed via an API endpoint. When a user submits a review, the application sends the text to the API and receives a classification in response. Then the sentiment is detected using the tfIdf algorithm.


Technologies used

Python Flask for the backend.
HTML, CSS and JavaScript for the frontend.
TfIdf algorithm for machine learning model training.
TextRank algorithm for text summarization.

Future improvements

Improve the accuracy of the emotion detection model.
Add support for multiple languages.
Incorporate sentiment analysis to provide more granular classifications of emotions.
Improve the UI to make it more user-friendly and visually appealing.

