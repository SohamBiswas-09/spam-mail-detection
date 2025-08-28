from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import os
import pandas as pd
import string
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Download stopwords
nltk.download('stopwords')
STOP_WORDS = set(stopwords.words('english'))

# Define text preprocessing function
def process_text(text: str):
    """Remove punctuation and stopwords from text."""
    nopunc = ''.join([char for char in text if char not in string.punctuation])
    clean_words = [word for word in nopunc.split() if word.lower() not in STOP_WORDS]
    return clean_words

# Load dataset
try:
    df = pd.read_csv('emails.csv')
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
except Exception as e:
    raise Exception("Error loading 'emails.csv'. Ensure the file exists and has 'text' and 'spam' columns.") from e

# Check if dataset contains the correct columns
if not set(['text', 'spam']).issubset(df.columns):
    raise Exception("Dataset must contain 'text' and 'spam' columns.")

# Vectorize text data
vectorizer = CountVectorizer(analyzer=process_text)
X = vectorizer.fit_transform(df['text'])
y = df['spam']

# Pickle model file
model_filename = 'spam_model.pkl'

# Load or train model
if os.path.exists(model_filename):
    with open(model_filename, 'rb') as f:
        classifier = pickle.load(f)
    print("Loaded classifier from pickle.")
else:
    classifier = MultinomialNB().fit(X, y)
    with open(model_filename, 'wb') as f:
        pickle.dump(classifier, f)
    print("Trained classifier and saved to pickle.")

# Initialize FastAPI app
app = FastAPI(title="Spam Detection API", description="A simple API to detect spam emails.")

# Enable CORS (needed for frontend requests)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (for testing)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define request model
class EmailMessage(BaseModel):
    text: str

# Define predict route
@app.post("/predict", summary="Predict if an email is spam or not")
def predict(email: EmailMessage):
    if not email.text.strip():  # Ensure text is not empty
        raise HTTPException(status_code=400, detail="Text field cannot be empty.")

    # Transform input text using vectorizer
    text_vector = vectorizer.transform([email.text])
    
    # Predict spam or not
    prediction = classifier.predict(text_vector)[0]

    return {"prediction": int(prediction)}

# Run with: uvicorn main:app --reload
