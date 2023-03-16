import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
import joblib
from sklearn.pipeline import Pipeline


# Load the dataset
data = pd.read_csv("/Users/nathaliliyanage/Downloads/tripadvisor_hotel_reviews.csv")

# Prepare the data for training and testing
X = data['Review']
y = data['Rating'].apply(lambda x: 'positive' if x >= 3 else 'negative')  # Convert numerical ratings to binary labels


# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Vectorize the text data
vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

#Save the vectorizer object as a joblib file
joblib.dump(vectorizer,"vectorizer.joblib")

# Train a linear support vector machine (SVM) classifier
classifier = LinearSVC()
classifier.fit(X_train, y_train)

# Evaluate the classifier on the testing set
y_pred = classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

#bhdfjsbhhgjbsjdgbjdsfg
joblib.dump(classifier,'sentiment-analysis.joblib')


