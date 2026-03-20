import streamlit as st
import numpy as np
import re
import pickle
from scipy.sparse import hstack

# Load model
lr = pickle.load(open("model.pkl", "rb"))
tfidf = pickle.load(open("tfidf.pkl", "rb"))

# Labels
emotion_labels = {
    0: "Happy 😊",
    1: "Sad 😢",
    2: "Angry 😡",
    3: "Fear 😨"
}

# Lexicon words
happy_words = ["happy","joy","smile","excited","cheerful"]
sad_words = ["sad","cry","lonely","depressed","down"]
angry_words = ["angry","hate","furious","rage","annoyed"]
fear_words = ["fear","scared","terrified","nervous","anxious"]

# Clean text
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    return text

# Lexicon features
def get_lexicon_features(text):
    words = text.split()
    return np.array([
        sum(w in happy_words for w in words),
        sum(w in sad_words for w in words),
        sum(w in angry_words for w in words),
        sum(w in fear_words for w in words)
    ]).reshape(1, -1)

# Prediction
def predict(text):
    cleaned = clean_text(text)
    tfidf_feat = tfidf.transform([cleaned])
    lex_feat = get_lexicon_features(cleaned)
    final = hstack([tfidf_feat, lex_feat])
    pred = lr.predict(final)[0]
    return emotion_labels[int(pred)]

# UI
st.title("🧠 Emotion Detection App")
st.markdown("### Enter text and detect emotion instantly")

user_input = st.text_area("Enter text:")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter text")
    else:
        result = predict(user_input)
        st.success(f"Emotion: {result}")

