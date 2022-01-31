import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('dAjEQ6_EpptKJB8ceaXoS5PaF7quI66HlGfVIT0Zbah3')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/instances/b573d54b-f1ac-41b7-a79e-24e011321be0')

def english_to_french(englishText):
    frenchtranslation = language_translator.translate(text=englishText ,model_id='en-fr').get_result()
    french_translation = frenchtranslation['translations'][0]['translation']
    return french_translation

def french_to_english(frenchText):
    englishtranslation = language_translator.translate(text=frenchText ,model_id='fr-en').get_result()
    english_translation = englishtranslation['translations'][0]['translation']
    return english_translation
