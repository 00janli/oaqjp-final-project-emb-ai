# Flask installation: pip install "Flask==2.2.2"
# Flask start: flask --app server --debug run

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():

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
    emotion_scores = ', '.join("'{}': {}".format(key, value) for key, value in response.items() if key != 'dominant_emotion')
    
    # Return a formatted string with emotions
    return "For the given statement, the system response is {}. The dominant emotion is {}.". format(emotion_scores, response['dominant_emotion'])

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)