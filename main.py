import dialogflow
import uuid
import os
from weather import weather
usersays = []

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="key_weather.json"
#Pegando a sessão atual
session = uuid.uuid1() 

def detect_intent_texts(project_id, session_id, texts, language_code):
    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)

    #caminho da sessão
    #print('Session path: {}\n'.format(session))

    for text in texts:

        text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
        query_input = dialogflow.types.QueryInput(text=text_input)
        response = session_client.detect_intent(session=session, query_input=query_input)

        # Formato de texto enviado pelo usuario
        #print('Query text: {}'.format(response.query_result.query_text))

        #Linha de codigo para mostrar qual intent entrou e o nivel de confidence 
        #print('Detected intent: {} (confidence: {})\n'.format(
        #response.query_result.intent.display_name,response.query_result.intent_detection_confidence))
        print('Bot : {}\n'.format(response.query_result.fulfillment_text))

while True:
    usersays.append(input('You :'))
    detect_intent_texts( 'weather-318f9', session, usersays, 'en')
    usersays.clear()

