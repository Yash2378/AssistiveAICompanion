# assistant.py
from voice_assistant import VoiceAssistant
from nlp_processing import NLPProcessor
from utils.speech_utils import speak

class AICompanion:
    def __init__(self):
        self.voice_assistant = VoiceAssistant()
        self.nlp_processor = NLPProcessor()

    def start_listening(self):
        print("AI Companion is listening... say 'stop' to exit.")
        while True:
            try:
                user_input = self.voice_assistant.listen()
                if user_input:
                    print(f"You said: {user_input}")
                    intent = self.nlp_processor.get_intent(user_input)
                    self.handle_intent(intent, user_input)
            except Exception as e:
                print(f"Error: {e}")

    def handle_intent(self, intent, text):
        if intent == 'write':
            openai_response = self.nlp_processor.get_openai_response(text)
            print(openai_response)
        elif intent == 'greeting':
            speak("Hello! How can I help you today?")
        elif intent == 'weather':
            speak("It's a sunny day with a high of 75 degrees.")
        elif intent == 'stop':
            speak("Goodbye!")
            exit(0)
        else:
            openai_response = self.nlp_processor.get_openai_response(text)
            speak(openai_response)
