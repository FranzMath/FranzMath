import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('apikey')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('URL')

def english_to_french(englishText):
    frenchtranslation = language_translator.translate(text=englishText ,model_id='en-fr').get_result()
    french_translation = frenchtranslation['translations'][0]['translation']
    return french_translation

def french_to_english(frenchText):
    englishtranslation = language_translator.translate(text=frenchText ,model_id='fr-en').get_result()
    english_translation = englishtranslation['translations'][0]['translation']
    return english_translation
