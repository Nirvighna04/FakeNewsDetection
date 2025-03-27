import streamlit as st
import requests
from bs4 import BeautifulSoup
import joblib
import numpy as np

# Load the trained model
model = joblib.load("fake_news_model.pkl")
user_input=""
# Function to extract text from a news link
def extract_text_from_link(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            # Extract visible text from the webpage
            paragraphs = soup.find_all("p")
            article_text = " ".join([p.get_text() for p in paragraphs])
            return article_text.strip()
        else:
            return None
    except Exception as e:
        st.error(f"Error extracting text from link: {e}")
        return None

# App title
st.title("Fake News Detection Platform")
st.markdown("Analyze news articles to detect if they are **Fake News** or **Real News**.")

# Input options: Text or Link
st.header("Input News Content")
option = st.radio("Choose how to input news content:", ["Text", "News Link"])

if option == "Text":
    user_input = st.text_area("Paste the news article text here:")
elif option == "News Link":
    news_link = st.text_input("Paste the news article link here:")
    if st.button("Extract Text from Link"):
        extracted_text = extract_text_from_link(news_link)
        if extracted_text:
            st.text_area("Extracted News Text:", extracted_text, height=300)
            user_input = extracted_text
        else:
            st.warning("Could not extract text from the provided link. Please try a different link.")

# Prediction
if st.button("Detect Fake News"):
    if option == "Text" and not user_input.strip():
        st.warning("Please enter some text to analyze.")
    elif option == "News Link" and not news_link.strip():
        st.warning("Please enter a news link to analyze.")
    else:
        # Pass the input text to the model
        vectorizer = joblib.load("vectorizer.pkl")
        # Transform the user input into the numeric format
        user_input_vectorized = vectorizer.transform([user_input])

        # Predict using the processed input
        prediction = model.predict(user_input_vectorized)

        # Display result
        if prediction[0] == 0:  # Assuming 0: Fake, 1: Real
            st.error("This news article is classified as: **Fake News** 🛑")
        else:
            st.success("This news article is classified as: **Real News** ✅")

# Footer
st.markdown("---")
