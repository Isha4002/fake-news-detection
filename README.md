# 📰 Fake News Detection System

A Machine Learning-based Fake News Detection System that classifies news articles as **Real** or **Fake** using **TF-IDF Vectorization** and **Logistic Regression**.

## 🚀 Features

- Detects whether a news article is Real or Fake
- Uses Natural Language Processing (NLP)
- TF-IDF based text vectorization
- Logistic Regression classifier
- Interactive Streamlit Web App
- Confidence score display

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- TF-IDF Vectorizer
- Logistic Regression

## 📂 Project Structure

```
fake-news-detection/
│
├── fake_news_app.py
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
└── README.md
```

## 📊 Dataset

Dataset contains real and fake news articles.

Features:
- Title
- Text
- Subject
- Date

Total Records: 44,000+ news articles

## ⚙️ Machine Learning Pipeline

1. Data Collection
2. Data Preprocessing
3. Dataset Merging
4. TF-IDF Vectorization
5. Train-Test Split
6. Logistic Regression Training
7. Model Evaluation
8. Streamlit Deployment

## 🎯 Model Performance

Confusion Matrix:

```
[[4663   70]
 [  56 4191]]
```

The model achieves high classification accuracy on unseen news articles.

## ▶️ Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run fake_news_app.py
```

## 🌐 Live Demo

[Add your Streamlit deployment link here:](https://fake-news-detection-gicdsgphrspxqxrxudgar7.streamlit.app/)

```
https://your-app-name.streamlit.app
```

## 👩‍💻 Author

**Isha Pal**

Machine Learning | Python | NLP

GitHub:
https://github.com/Isha4002
