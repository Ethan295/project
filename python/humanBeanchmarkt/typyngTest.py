import pyautogui
import easyocr
import time
import os
import cv2
import numpy as np



# Cattura uno screenshot del rettangolo con coordinate 780,350 e 1750,530
screenshot = pyautogui.screenshot(region=(780, 350, 1750 - 780, 530 - 350))

# Salva lo screenshot in un file immagine
image_path = "screenshot.png"
screenshot.save(image_path)

# Carica l'immagine utilizzando OpenCV
image = cv2.imread(image_path)

# Applica operazioni di pre-elaborazione
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Conversione in scala di grigi
blur_image = cv2.GaussianBlur(gray_image, (5, 5), 0)  # Riduzione del rumore con filtro Gaussiano

# Applica un filtro di sharpening per migliorare la nitidezza
sharpened_image = cv2.addWeighted(gray_image, 1.5, blur_image, -0.7, 5)

# Binarizza l'immagine con un metodo di soglia (puoi sperimentare con il valore di soglia)
_, binarized_image = cv2.threshold(sharpened_image, 100, 240, cv2.THRESH_BINARY)

# Salva l'immagine pre-elaborata (facoltativo)
cv2.imwrite("preprocessed.png", binarized_image)

# Utilizza easyocr per riconoscere il testo nell'immagine pre-elaborata
reader = easyocr.Reader(['en'])
results = reader.readtext(binarized_image)

# Estrai il testo riconosciuto
text = " ".join(result[1] for result in results)

# Stampa il testo riconosciuto
print(text)

# Elimina l'immagine
os.remove(image_path)
#os.remove("preprocessed.png")

# Inserisci il testo riconosciuto nel campo desiderato (rimuovi il commento se necessario)
#pyautogui.write(text, interval=0.07)
