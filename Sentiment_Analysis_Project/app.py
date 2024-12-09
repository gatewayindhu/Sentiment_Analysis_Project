from flask import Flask, render_template, request, jsonify
from sentiment_module import SentimentAnalyzer

app = Flask(__name__)
analyzer = SentimentAnalyzer()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    review = data.get("review", "")
    if not review:
        return jsonify({"error": "No review provided"}), 400
    sentiment = analyzer.predict_sentiment(review)
    return jsonify({"sentiment": sentiment})

if __name__ == "__main__":
    app.run(debug=True)
