import io
import cv2
import pyautogui
import easyocr
import os
import time
import numpy as np

time.sleep(1)
x= 0
pyautogui.click(1270, 530)
for i in range(0, 20):
    screenshot = pyautogui.screenshot(region=(960, 340, 1680 - 960, 450 - 340))


    # Creare un oggetto di tipo file in memoria
    image_stream = io.BytesIO()
    screenshot.save(image_stream, format="PNG")
    image_stream.seek(0)

    # Carica l'immagine direttamente da memoria utilizzando OpenCV
    image = cv2.imdecode(np.frombuffer(image_stream.read(), np.uint8), -1)

    # Altri passaggi di elaborazione dell'immagine rimangono invariati
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
    sharpened_image = cv2.addWeighted(gray_image, 1.5, blur_image, -0.7, 5)
    _, binarized_image = cv2.threshold(sharpened_image, 100, 240, cv2.THRESH_BINARY)

    # Utilizza easyocr per riconoscere il testo nell'immagine pre-elaborata
    reader = easyocr.Reader(['en'])
    results = reader.readtext(binarized_image)

    text = " ".join(result[1] for result in results)

    time.sleep(2 + x)
    pyautogui.write(text, interval=0.2)

    pyautogui.press('enter')
    pyautogui.press('enter')

    x += 0.9
       

    print(text)
