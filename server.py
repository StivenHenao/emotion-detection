"""Flask app for detecting emotions in a given text input."""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion detector")

@app.route("/emotionDetector")
def sent_detector():
    """Endpoint that analyzes the emotional content of a given text."""
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        return "Invalid text! Please try again!"

    response = emotion_detector(text_to_analyze)

    if not response or 'dominant_emotion' not in response:
        return "Invalid response from emotion detector. Please try again."

    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']}, "
        f"and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    """Render the index HTML page."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
