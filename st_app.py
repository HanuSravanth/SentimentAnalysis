import streamlit as st
from transformers import pipeline

st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",)


sentiment_classifier = pipeline('sentiment-analysis')

# set title for the app
st.title("""Sentiment Classifier App""")
st.markdown("---")

# take input
form = st.form(key='sentiment-form')
user_input = form.text_area('Enter your text')
submit = form.form_submit_button('Submit')

# fetch sentiment from model
if submit:
    classifier = pipeline("sentiment-analysis")
    result = classifier(user_input)[0]
    label = result['label']
    score = result['score']
    if label == 'POSITIVE':
        st.success(f'{label} sentiment (score: {score})')
    else:
        st.error(f'{label} sentiment (score: {score})')