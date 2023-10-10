import pyautogui
import os
from PIL import Image
import time

# Definisci le coordinate della regione dello screenshot
x1, y1, x2, y2 = 800, 150, 1800, 650


search = region=(x1, y1, x2 - x1, y2 - y1)

clic_effettuati = 0

time.sleep(1)

pyautogui.click(1250, 400)



while clic_effettuati < 31:

        screenshot = pyautogui.screenshot(region=(x1, y1, x2 - x1, y2 - y1))

        target_location = pyautogui.locateOnScreen('python/humanBeanchmarkt/bersaglio.png', region=(x1, y1, x2 - x1, y2 - y1), grayscale=True, confidence=0.8)

        if target_location is not None:
            pyautogui.click(pyautogui.center(target_location))
            clic_effettuati += 1
             


