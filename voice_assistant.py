# voice_assistant.py
import speech_recognition as sr
from utils.speech_utils import speak

class VoiceAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.recognizer.listen(source)
        try:
            text = self.recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that. Could you please repeat?")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        return None
