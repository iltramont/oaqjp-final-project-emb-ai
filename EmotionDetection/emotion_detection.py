"""Function for analyse text"""

import json
import requests

def emotion_detector(text_to_analyse):
    """Analyse the input text"""
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
        }
    myobj = {
        'raw_document': {'text': text_to_analyse}
    }
    response = requests.post(url, json=myobj, headers=header)
    if response.status_code == 400:
        return {
            "anger": None, 
            "disgust": None, 
            "fear": None, 
            "joy": None, 
            "sadness": None, 
            "dominant_emotion": None
        }           
    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    dominant_emotion = ''
    max_score = -1.0
    for emotion, score in emotions.items():
        if score > max_score:
            max_score = score
            dominant_emotion = emotion
    emotions['dominant_emotion'] = dominant_emotion
    return emotions
