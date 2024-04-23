# app/emotion.py

from ibm_watson import NaturalLanguageUnderstandingV1 as NLU
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Setup IBM Watson credentials
authenticator = IAMAuthenticator('your_api_key')
nlu_client = NLU(version='2022-04-07', authenticator=authenticator)
nlu_client.set_service_url('your_service_url')

def emotion_predictor(text):
    try:
        response = nlu_client.analyze(
            text=text,
            features=Features(emotion=EmotionOptions())).get_result()
        emotions = response['emotion']['document']['emotion']
        formatted_output = {
            "text": text,
            "emotions": emotions
        }
        return formatted_output
    except Exception as e:
        return {"error": str(e)}
