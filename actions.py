import webbrowser
import pywhatkit
import datetime
import os
import requests
import urllib.parse
from config import CITY, WEATHER_API_KEY

def execute(command):
    cmd = command.lower()


    if "tik tok" in cmd or "tt" in cmd or "tiktok" in cmd:
        webbrowser.open("https://www.tiktok.com/explore")
        return "Abriendo Tik tok."
    
    if "facebook" in cmd or "fb" in cmd:
        webbrowser.open("https://facebook.com")
        return "Abriendo Facebook."

    if "whatsapp" in cmd or "wasap" in cmd:
        webbrowser.open("https://web.whatsapp.com/")
        return "Abriendo WhatsApp."

    if "mejorcolegio" in cmd or "cualeselmejorcolegio" in cmd or "dónde están los mejores" in cmd or "dónde están los mejores estudiantes" in cmd or "mejor colegio" in cmd:
        webbrowser.open("https://www.facebook.com/uejuandevelasco/")
        return "Buscando el mejor colegio."

    if "youtube" in cmd:
        webbrowser.open("https://youtube.com")
        return "Abriendo YouTube."
    
    if "informaticajuvenil" in cmd or "informatica" in cmd or "licenluis" in cmd or "licendoris" in cmd:
        webbrowser.open("https://jdvinformatica.com/")
        return "Viendo quien es el mejor colegio."

    if "reproduce" in cmd:
        idx = cmd.find("reproduce")
        query = command[idx + len("reproduce"):].strip()
        try:
            pywhatkit.playonyt(query)
            return f"Reproduciendo {query}"
        except Exception:
            return "No pude reproducir en YouTube."
        
    if "imagenes" in cmd or "imágenes" in cmd or "imagen" in cmd:
        keys = ["imágenes", "imagenes", "imagen"]
        found = [(cmd.find(k), k) for k in keys if k in cmd]
        idx, key = min(found, key=lambda t: t[0]) if found else (-1, "")
        query = command[idx + len(key):].strip() if idx >= 0 else ""
        try:
            if query:
                q = urllib.parse.quote_plus(query)
                url = f"https://www.google.com/search?tbm=isch&q={q}"
                webbrowser.open(url)
                return f"Abriendo imágenes de {query}"
            else:
                webbrowser.open("https://www.google.com/imghp?hl=es")
                return "Abriendo Google Imágenes."
        except Exception:
            return "No pude abrir las imágenes."

    if "busca" in cmd or "buscar" in cmd or "consultar" in cmd or "consulta" in cmd:
        keys = ["buscar", "busca", "consultar", "consulta"]
        found = [(cmd.find(k), k) for k in keys if k in cmd]
        idx, key = min(found, key=lambda t: t[0]) if found else (-1, "")
        query = command[idx + len(key):].strip() if idx >= 0 else ""
        try:
            if query:
                q = urllib.parse.quote_plus(query)
                url = f"https://www.google.com/search?q={q}&hl=es"
                webbrowser.open(url)
                return f"Buscando {query} en Google."
            else:
                webbrowser.open("https://www.google.com/?hl=es")
                return "Abriendo Google."
        except Exception:
            return "No pude buscarlo."

    if "hora" in cmd:
        hora = datetime.datetime.now().strftime("%H:%M")
        return f"Son las {hora}"

    if "temperatura" in cmd or "clima" in cmd:
        if not WEATHER_API_KEY:
            return "No hay API key configurada para el clima."
        url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={WEATHER_API_KEY}&units=metric&lang=es"
        try:
            r = requests.get(url, timeout=8)
            data = r.json()
            if data.get("cod") == 200:
                temp = data["main"]["temp"]
                desc = data["weather"][0]["description"]
                return f"La temperatura actual en {CITY} es {temp} grados con {desc}"
            else:
                return "No pude obtener la temperatura."
        except Exception:
            return "Error al consultar el clima."

    if "carpeta de descargas" in cmd:
        os.startfile(os.path.expanduser("~/Downloads"))
        return "Abriendo carpeta de descargas."

    if "abre carpeta" in cmd:
        ruta = os.path.join(os.path.expanduser("~"), "Desktop")
        os.startfile(ruta)
        return "Carpeta abierta."

    return None
