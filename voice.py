import speech_recognition as sr
import pyttsx3
from config import NAME
import face

engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    global engine
    print(f"{NAME}:", text)
    try:
        try:
            face.set_speaking(True)
        except Exception:
            pass
        engine.say(text)
        engine.runAndWait()
    except Exception:
        try:
            # Reintenta re-inicializando el motor si falló
            engine = pyttsx3.init()
            engine.setProperty('rate', 170)
            engine.say(text)
            engine.runAndWait()
        except Exception:
            pass
    finally:
        try:
            face.set_speaking(False)
        except Exception:
            pass

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        r.adjust_for_ambient_noise(source, duration=0.5)

        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
        except:
            return ""

    try:
        text = r.recognize_google(audio, language="es-ES")
        print("Usted:", text)
        return text.lower()
    except:
        return ""
