from brain import think
from voice import speak, listen
from actions import execute
from config import NAME
import random

ASSISTANT_NAME = NAME.lower()

activation_responses = [
    "Sí señor.",
    "Le escucho.",
    "A su servicio.",
    "Operativo.",
    "Listo."
]


def main():
    print(f"{NAME} iniciado...")
    while True:
        user_input = listen()
        if not user_input:
            continue
        if "adiós" in user_input:
            speak("Desconectando sistemas. Hasta luego, señor.")
            break
        command = user_input
        if ASSISTANT_NAME in user_input:
            command = user_input.replace(ASSISTANT_NAME, "").strip()
            if command == "":
                speak(random.choice(activation_responses))
                continue
        action_response = execute(command)
        if action_response:
            speak(action_response)
        else:
            response = think(command)
            speak(response)


if __name__ == "__main__":
    main()
