from transformers import pipeline

print("imports complete...")
sentiment_classifier = pipeline('sentiment-analysis', model="distilbert-base-uncased-finetuned-sst-2-english")

print( sentiment_classifier(["Yay! This is my first transformers snippet!"]) )


import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"])

st.bar_chart(chart_data)