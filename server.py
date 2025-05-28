""" Server.py for Emotion Detector training project 
    Coursera: IBM Developing AI Applications with Python and Flask """

# Flask installation: pip install "Flask==2.2.2"
# Flask start: flask --app server --debug run
# Install PyLint: python3.11 -m pip install pylint

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """  The response is displayed as:
    For the given statement, the system response is 
    'anger': 0.006274985, 'disgust': 0.0025598293,
    'fear': 0.009251528, 'joy': 0.9680386 and 
    'sadness': 0.049744144. The dominant emotion is joy. """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    response = {
        "anger": response.get("anger"),
        "disgust": response.get("disgust"),
        "fear": response.get("fear"),
        "joy": response.get("joy"),
        "sadness": response.get("sadness"),
        "dominant_emotion": response.get("dominant_emotion")
    }

    # Build and format a string of emotion scores excl. dominant_emotion
    emotion_score_items = []
    for key, value in response.items():
        if key != 'dominant_emotion':
            score_item = f"'{key}': {value}"
            emotion_score_items.append(score_item)

    emotion_scores = ', '.join(emotion_score_items)

    # The old one looong line code
    # emotion_scores = ', '.join("'{}': {}".format(key, value) for key, value
    # in response.items() if key != 'dominant_emotion')

    # Check if the label is None, indicating an error or invalid input
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Return a formatted string with emotions
    emotion_scores_part = f"For the given statement, the system response is {emotion_scores}."
    dominant_emotion_part = f"The dominant emotion is <b>{response['dominant_emotion']}</b>."
    return f"{emotion_scores_part} {dominant_emotion_part}"

    # The old one looong line code
    # return "For the given statement, the system response is {}.
    # The dominant emotion is <b>{}</b>.". format(emotion_scores, response['dominant_emotion'])

@app.route("/")
def render_index_page():
    """ Index page """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
