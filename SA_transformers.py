from transformers import pipeline

sentiment_classifier = pipeline('sentiment-analysis')

sentiment_classifer(["Yay! This is my first transformers snippet!"])