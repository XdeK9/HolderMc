import pyautogui
import keyboard
import time
import threading

clicking = False

def hold_click():
    while True:
        if clicking:
            pyautogui.mouseDown(button='left')  # Click Holdé
            while clicking:
                time.sleep(0.1)
            pyautogui.mouseUp(button='left')  # Click non Holdé
        time.sleep(0.1)

def toggle_click():
    global clicking
    clicking = not clicking
    print("Clic maintenu" if clicking else "Clic relâché")

threading.Thread(target=hold_click, daemon=True).start()

# La Touche
keyboard.add_hotkey('F9', toggle_click)

# Pour que le script soit toujours allumé sauf si tu fermes le script
keyboard.wait()
