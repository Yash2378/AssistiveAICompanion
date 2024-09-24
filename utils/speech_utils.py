# utils/speech_utils.py
from gtts import gTTS
import pygame
import os

pygame.mixer.init()

def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = 'temp_voice.mp3'
    tts.save(filename)
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
    os.remove(filename)
