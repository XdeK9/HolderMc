import pyautogui
import keyboard
import time
import threading

clicking = False

def hold_click():
    while True:
        if clicking:
            pyautogui.mouseDown(button='left')  # Maintient appuyé
            while clicking:
                time.sleep(0.1)
            pyautogui.mouseUp(button='left')  # Relâche quand désactivé
        time.sleep(0.1)

def toggle_click():
    global clicking
    clicking = not clicking
    print("Clic maintenu" if clicking else "Clic relâché")

# Lancer le thread de clic
threading.Thread(target=hold_click, daemon=True).start()

# Activer/désactiver avec F9
keyboard.add_hotkey('F9', toggle_click)

# Garde le script en vie
keyboard.wait()
