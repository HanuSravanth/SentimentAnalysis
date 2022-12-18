import streamlit as st
from transformers import pipeline

st.set_page_config(
    page_title="Sentiment Classifier",
    page_icon="🤗",
    layout="wide",
    initial_sidebar_state="expanded",)

# set title for the app
st.title("""🤗 Sentiment Classifier App""")
st.markdown("---")
st.markdown("## Input")

# take input
form = st.form(key='sentiment-form')
user_input = form.text_area('Enter text here')
submit = form.form_submit_button('Submit')
st.markdown("---")
st.markdown("## Result")

# fetch sentiment from model
if submit:
    classifier = pipeline("sentiment-analysis")
    result = classifier(user_input)[0]
    label = result['label']
    score = result['score']
    c1, c2, c3 = st.columns([50, 50, 100])
    if label == 'POSITIVE':
        with c1: st.success(f"Sentiment: {label} 😇")
        with c2: st.success(f"Score: {(score * 100):.2f}%")
    else:
        with c1: st.error(f"Sentiment: {label} 😑")
        with c2: st.error(f"Score: {(score * 100):.2f}%")


