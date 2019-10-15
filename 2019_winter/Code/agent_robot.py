import dialogflow
import speech_recognition as sr
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import os


def main():

    # get input spech from user
    input_speech = detect_audio()
    print("what you said: %s"  %input_speech)

    # pass input speech to dialog flow and return google's response
    google_response = detect_intent_texts("robotics-test-agent", 123, [input_speech], "en")
    print("what google said is: %s" %google_response)

    # respond with voice
    speech_command = "flite -t \"" + google_response + "\""
    print(speech_command)
    os.system(speech_command)
    
def detect_intent_texts(project_id, session_id, texts, language_code):
    """Returns the result of detect intent with texts as inputs.

    Using the same `session_id` between requests allows continuation
    of the conversation."""

    import dialogflow_v2 as dialogflow
    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)
    print('Session path: {}\n'.format(session))

    for text in texts:
        text_input = dialogflow.types.TextInput(
            text=text, language_code=language_code)

        query_input = dialogflow.types.QueryInput(text=text_input)

        response = session_client.detect_intent(
            session=session, query_input=query_input)

        # UNCOMMENT FOR DEBUG
        #print('=' * 20)
        #print('Query text: {}'.format(response.query_result.query_text))
        #print('Detected intent: {} (confidence: {})\n'.format(
        #    response.query_result.intent.display_name,
        #    response.query_result.intent_detection_confidence))
        #print('Fulfillment text: {}\n'.format(
        #    response.query_result.fulfillment_text))

    return response.query_result.fulfillment_text

def detect_audio():
    # obtain audio from the microphone
    response = ""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #print("Please wait. Calibrating microphone...")
        # listen for 1 second and create the ambient noise energy level
        r.adjust_for_ambient_noise(source, duration=1)
        print("Say something!")
        audio = r.listen(source,phrase_time_limit=5)
 
        # recognize speech using Sphinx/Google
    try:
        #response = r.recognize_sphinx(audio)
        response = r.recognize_google(audio)
        
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))

    return response

if __name__ == "__main__":
    main()
