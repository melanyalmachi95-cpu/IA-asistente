from config import SYSTEM_PROMPT

MODEL = "llama3"

import subprocess

def think(text):
    prompt = f"{SYSTEM_PROMPT}\nUsuario: {text}"
    result = subprocess.run(
        ["ollama", "run", MODEL],
        input=prompt,
        text=True,
        encoding="utf-8",
        capture_output=True
    )
    output = result.stdout.strip() if result.stdout else ""
    err = result.stderr.strip() if result.stderr else ""
    return output if output else err
