import streamlit as st
from textblob import TextBlob

# Set up the Streamlit app
st.title('Sentiment Analysis App')
st.write('Enter some text and I will analyze the sentiment for you!')

# Get user input
user_input = st.text_area('Enter your text here')

# Analyze sentiment
if st.button('Analyze'):
    if user_input:
        blob = TextBlob(user_input)
        sentiment = blob.sentiment.polarity
        if sentiment > 0:
            st.write('Sentiment: Positive')
        elif sentiment < 0:
            st.write('Sentiment: Negative')
        else:
            st.write('Sentiment: Neutral')
    else:
        st.write('Please enter some text to analyze.')
