import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyse):
    """Define a function named sentiment_analyzer that takes a string input (text_to_analyse)."""
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # URL of the sentiment analysis service
    myobj = { "raw_document": { "text": text_to_analyse } }
    # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Set the headers required for the API request
    response = requests.post(url, json = myobj, headers=header)
    # Send a POST request to the API with the text and headers
    #return response.text
    response = requests.post(url, json=myobj, headers=header) # Return the response text from the API
    if response.status_code == 400:
        return {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
        }
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)
    #print(formatted_response)
    # Extracting sentiment emotion scores from the response
    anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
    disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
    joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
    sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']
    emotion_score_list = [anger_score, disgust_score, fear_score, joy_score, sadness_score]
    dominant_emotion_score = max(emotion_score_list)
    if dominant_emotion_score == anger_score:
        dominant_emotion = "anger"
    elif dominant_emotion_score == disgust_score:
        dominant_emotion = "disgust"
    elif dominant_emotion_score == fear_score:
        dominant_emotion = "fear"
    elif dominant_emotion_score == joy_score:
        dominant_emotion = "joy"
    elif dominant_emotion_score == sadness_score:
        dominant_emotion = "sadness"
    # Returning a dictionary containing emotion analysis results
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
#print(emotion_detector("I think I am having fun."))