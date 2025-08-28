# 📧 Spam Mail Detector

A simple and effective Spam Mail Detection system that classifies emails as **Spam** or **Not Spam** using machine learning techniques.

## 🚀 Features

- Detects spam emails based on content
- Uses Natural Language Processing (NLP) for text preprocessing
- Trained using popular ML algorithms (e.g., Naive Bayes, Logistic Regression)
- Supports prediction on custom inputs
- Lightweight and easy to integrate into web apps

## 🛠️ Tech Stack

- Python 🐍
- scikit-learn 🤖
- Pandas & NumPy 📊
- Flask / FastAPI (optional, for web deployment)
- Jupyter Notebook (for training and visualization)

## 📂 Project Structure
SpamMailDetector/
│
├── __pycache__/              # Compiled Python files
│   └── main.cpython-*.pyc
│
├── venv/                     # Virtual environment (should be in .gitignore)
│   ├── Include/
│   ├── Lib/
│   ├── Scripts/
│   └── pyvenv.cfg
│
├── .dockerignore             # Docker ignore file
├── docker-compose.yml        # Docker Compose config (multi-container setup)
├── Dockerfile                # Dockerfile for containerizing the app
│
├── emails.csv                # Dataset file
├── index.html                # HTML frontend
├── main.py                   # Main Python app script (likely backend logic)
├── script.js                 # JavaScript frontend script
├── style.css                 # CSS styles
│
├── spam_model.pkl            # Trained ML model file
├── requirements.txt          # Python dependencies
└── README.md                 # Project overview



## 📈 Dataset

We used the **[SpamAssassin Public Corpus](https://spamassassin.apache.org/publiccorpus/)** and other open datasets for training.

> You can also upload your own dataset in CSV format with `text` and `label` columns.

## 🧠 How It Works

1. **Preprocessing** – Cleans the text (stop words, punctuation, etc.)
2. **Vectorization** – Converts text into numerical form using `TfidfVectorizer`
3. **Model Training** – Trains a classifier (e.g., Multinomial Naive Bayes)
4. **Prediction** – Returns label: `Spam` or `Not Spam`

## 🔧 Installation

```bash
git clone https://github.com/ShubhamShaw01/SpamMailDetector.git
cd SpamMailDetector
pip install -r requirements.txt
