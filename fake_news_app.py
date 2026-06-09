import streamlit as st
import pickle

# Load Saved Model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

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
