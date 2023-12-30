## instalações
# pip install SpeechRecognition pyaudio spacy transformers pyttsx3 --user
# python -m pip install --user nltk
# python -m pip install --user rasa --upgrade --no-deps
# pip install ruamel.yaml


## importações
import nltk
from nltk.tokenize import word_tokenize 
import speech_recognition as sr
import pyaudio
import spacy
from transformers import pipeline
import pyttsx3
from rasa.nlu import Interpreter
import ast

## código de partida
# Inicializar o reconhecimento de voz

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
recognizer = sr.Recognizer()

# Inicializar o interpretador Rasa NLU
interpreter = Interpreter.load("path/to/nlu/model")

# Inicializar o mecanismo de síntese de fala
engine = pyttsx3.init()
nlp = spacy.load("en_core_web_sm")

# Função para reconhecimento de voz
def recognize_speech():
    with sr.Microphone() as source:
        print("Fale algo...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("Você disse:", text)
        return text
    except sr.UnknownValueError:
        print("Não foi possível entender a fala")
    except sr.RequestError as e:
        print(f"Erro no reconhecimento de fala: {e}")

# Função para análise gramatical usando NLTK
def analyze_text(text):
    tokens = word_tokenize(text)
    tagged_tokens = nltk.pos_tag(tokens)
    return tagged_tokens

# Função para síntese de fala
def text_to_speech(text):
    engine.say(text)
    engine.runAndWait()

def check_and_correct_code_with_rasa(code):
    # Enviar a consulta para o modelo Rasa NLU
    response = interpreter.parse(code)
    
    # Verificar a intenção identificada pelo modelo
    intent = response["intent"]["name"]

    if intent == "verificar_codigo":
        # Extrair a entidade relacionada ao código
        code_entity = next((entity for entity in response["entities"] if entity["entity"] == "code"), None)

        if code_entity:
            # Verificar e corrigir o código
            code_to_check = code_entity["value"]
            try:
                parsed_code = ast.parse(code_to_check)
                return "O código está correto."
            except SyntaxError as e:
                return f"Erro de sintaxe no código: {e}"
            except Exception as e:
                return f"Erro ao analisar o código: {e}"
        else:
            return "Não foi possível identificar o código a ser verificado."
    else:
        return "Não foi possível entender a intenção relacionada à verificação de código."

def create_and_improve_text(input_text):
    # Implemente aqui as melhorias desejadas no texto
    improved_text = input_text  # Neste exemplo, o texto não é alterado
    return improved_text

def process_command(command):
    response = interpreter.parse(command)
    return response["intent"]["name"], response["entities"]

# Exemplo de uso
while True:
    user_command = recognize_speech()
    print("Comando do usuário:", user_command)

    intent, entities = process_command(user_command)

    if intent == "cumprimento":
        response = "Olá! Como posso ajudar você?"
    elif intent == "clima":
        response = "Desculpe, eu não tenho acesso à previsão do tempo no momento."
    elif intent == "verificar_codigo":
        # Extrair a entidade relacionada ao código
        code_entity = next((entity for entity in entities if entity["entity"] == "code"), None)

        if code_entity:
            # Verificar e corrigir o código usando a função específica
            response = check_and_correct_code_with_rasa(code_entity["value"])
        else:
            response = "Não foi possível identificar o código a ser verificado."
    elif intent == "melhorar_texto":
        # Extrair a entidade relacionada ao texto
        text_entity = next((entity for entity in entities if entity["entity"] == "text"), None)

        if text_entity:
            # Melhorar o texto usando a função específica
            response = create_and_improve_text(text_entity["value"])
        else:
            response = "Não foi possível identificar o texto a ser melhorado."
    else:
        response = "Desculpe, não entendi. Pode repetir?"

    print("Resposta do Chatbot:", response)
    # Sintetizar a resposta do Chatbot
    text_to_speech(response)