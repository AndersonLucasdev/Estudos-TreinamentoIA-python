## instalações
# pip install SpeechRecognition PyAudio
# pip install PyAudio
# pip install spacy
# python -m spacy download en_core_web_sm  # Modelo para inglês
# pip install transformers
# pip install pyttsx3

## importações
# import speech_recognition as sr
# import pyaudio
# import spacy
# from transformers import pipeline
# import pyttsx3

###

## código de partida
# Inicializar o reconhecimento de voz

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
recognizer = sr.Recognizer()

# Inicializar o mecanismo de síntese de fala
engine = pyttsx3.init()
nlp = spacy.load("en_core_web_sm")