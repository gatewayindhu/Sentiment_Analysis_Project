from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import numpy as np

class SentimentAnalyzer:
    def __init__(self):
        # Sample dataset for demonstration
        self.data = [
            ("This product is amazing!", "positive"),
            ("I love this product, highly recommend it!", "positive"),
            ("Terrible experience, do not buy.", "negative"),
            ("Not worth the price.", "negative"),
            ("It's okay, could be better.", "neutral"),
            ("nice ", "positive"),
            (" very nice ", "positive"),
        ]
        self.vectorizer = CountVectorizer()
        self.model = MultinomialNB()
        self._train_model()

    def _train_model(self):
        # Extract features and labels
        texts, labels = zip(*self.data)
        X = self.vectorizer.fit_transform(texts)
        y = np.array([1 if label == "positive" else -1 if label == "negative" else 0 for label in labels])
        self.model.fit(X, y)

    def predict_sentiment(self, text):
        X = self.vectorizer.transform([text])
        prediction = self.model.predict(X)[0]
        sentiment = {1: "positive", -1: "negative", 0: "neutral"}
        return sentiment[prediction]
