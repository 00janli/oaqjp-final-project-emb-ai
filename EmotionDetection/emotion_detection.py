# Install requests: python3 -m pip install requests

import requests # Import the requests library to handle HTTP requests
import json     # Import the json package to handle JSON format

def emotion_detector(text_to_analyze):  # Function to analyze emotions in text
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of Watson NLP EmotionPredict
    myobj = { "raw_document": { "text": text_to_analyze } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    
    # return response.text  # Return the response text from the API
    formatted_response = json.loads(response.text)  # Parsing the JSON response from the API

    # Extracting emotions from the response
    # If the response status code is 200, extract the emotions from the response
    if response.status_code == 200:
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotions, key=emotions.get)  # Find the dominant emotion

    # If the response status code is 400, set scores and dominant emotion to None
    elif response.status_code == 400:
        emotions = {key: None for key in ['emotion']}
        dominant_emotion = None

    result = { **emotions, 'dominant_emotion': dominant_emotion }  # Combining the final result

    return result
    