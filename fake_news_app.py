import streamlit as st
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load Dataset
fake = pd.read_csv(
    r"C:\Users\ishap\Downloads\archive\Fake.csv"
)

true = pd.read_csv(
    r"C:\Users\ishap\Downloads\archive\True.csv"
)

# Labels
fake["label"] = 0
true["label"] = 1

# Merge Dataset
df = pd.concat([fake, true])

# Create Content Column
df["content"] = df["title"] + " " + df["text"]

# Features & Labels
X = df["content"]
y = df["label"]

# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Vectorization
vectorizer = TfidfVectorizer(
    stop_words="english",
    max_df=0.7
)

X_train = vectorizer.fit_transform(X_train)

# Train Model
model = LogisticRegression()

model.fit(X_train, y_train)

# UI
st.title("📰 Fake News Detection System")

st.write(
    "Enter a news article and check whether it is Real or Fake."
)

news = st.text_area(
    "Enter News Article"
)

if st.button("Check News"):

    if news.strip() == "":
        st.warning("Please enter news text.")
    else:

        news_vector = vectorizer.transform([news])

        prediction = model.predict(news_vector)

        probability = model.predict_proba(news_vector)

        confidence = round(
            max(probability[0]) * 100,
            2
        )

        if prediction[0] == 1:
            st.success(
                f"✅ REAL NEWS\n\nConfidence: {confidence}%"
            )
        else:
            st.error(
                f"❌ FAKE NEWS\n\nConfidence: {confidence}%"
            )

        st.progress(confidence / 100)

    