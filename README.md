# 📰 Fake News Detection System

A Machine Learning-based Fake News Detection System that classifies news articles as **Real** or **Fake** using **Natural Language Processing (NLP)** techniques.

The project uses **TF-IDF Vectorization** and **Logistic Regression** to analyze news content and predict its authenticity. The model is deployed as an interactive web application using **Streamlit**.

---

## 🚀 Live Demo

🌐 Live Application:

[Fake News Detection System](https://fake-news-detection-gicdsgphrspxqxrxudgar7.streamlit.app)

---

## 📌 Features

✅ Detects Fake and Real News Articles

✅ NLP-based Text Processing

✅ TF-IDF Feature Extraction

✅ Logistic Regression Classification

✅ Confidence Score Display

✅ Interactive Streamlit Web Interface

✅ Deployed on Streamlit Cloud

---

## 🛠️ Tech Stack

### Programming Language

- Python

### Libraries

- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Pickle

### Machine Learning

- TF-IDF Vectorization
- Logistic Regression

### Tools

- Jupyter Notebook
- GitHub
- Streamlit Cloud

---

## 📂 Project Structure

```text
fake-news-detection/
│
├── Fake-News-Detection.ipynb
├── fake_news_app.py
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
└── README.md
```

---

## 📊 Dataset

The dataset contains both real and fake news articles.

Dataset Features:

| Column | Description |
|----------|-------------|
| title | News Headline |
| text | News Content |
| subject | News Category |
| date | Publication Date |

Total Records:

- Fake News: 23,481
- Real News: 21,417
- Total: 44,898+

---

## ⚙️ Machine Learning Workflow

### 1. Data Collection

Loaded Fake and Real news datasets.

### 2. Data Labeling

Assigned labels:

```python
Fake = 0
Real = 1
```

### 3. Data Merging

Merged both datasets into a single dataframe.

### 4. Text Feature Creation

Created a content column:

```python
content = title + text
```

### 5. Train-Test Split

```python
test_size = 20%
```

Training Samples:

```text
35918
```

Testing Samples:

```text
8980
```

### 6. TF-IDF Vectorization

Converted text data into numerical vectors using:

```python
TfidfVectorizer()
```

### 7. Model Training

Trained a Logistic Regression model:

```python
LogisticRegression()
```

### 8. Model Evaluation

Generated predictions and confusion matrix.

---

## 📈 Results

### Confusion Matrix

```text
[[4663   70]
 [  56 4191]]
```

### Model Accuracy

```text
98.60%
```

The model successfully classifies most news articles with high accuracy.

---

## 🖥️ Application Preview

### Home Screen

Add Screenshot Here

### Prediction Example

Add Screenshot Here

---

## ▶️ Run Locally

### Clone Repository

```bash
git clone https://github.com/Isha4002/fake-news-detection.git
```

### Move into Project Folder

```bash
cd fake-news-detection
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit App

```bash
streamlit run fake_news_app.py
```

---

## 📦 Required Dependencies

```text
streamlit
pandas
numpy
scikit-learn
```

---

## 🎯 Future Improvements

- Deep Learning Models (LSTM/BERT)
- News Source Verification
- News Category Classification
- Improved UI Design
- Real-Time News API Integration

---

## 👩‍💻 Author

### Isha Pal

Machine Learning Enthusiast | Python Developer | NLP Learner

GitHub:

https://github.com/Isha4002

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.
