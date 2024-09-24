# nlp_processing.py
import spacy
from utils.openai_utils import get_openai_response

class NLPProcessor:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.conversation_history = []

    def get_intent(self, text):
        doc = self.nlp(text)
        if "write down" in text.lower():
            return 'write'
        elif any(word.text.lower() in ['hi', 'hello', 'hey'] for word in doc):
            return 'greeting'
        elif 'weather' in text.lower():
            return 'weather'
        elif 'stop' in text.lower():
            return 'stop'
        return 'unknown'

    def get_openai_response(self, query):
        return get_openai_response(query, self.conversation_history)
