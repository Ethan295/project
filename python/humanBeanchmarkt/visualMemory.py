import pyautogui
import time
from PIL import ImageGrab

# Imposta le coordinate del rettangolo
x1, y1 = 1000, 200
x2, y2 = 1500, 650

# Funzione per verificare se un pixel è bianco (con tutti i canali > 200)
def is_white_pixel(pixel):
    return all(value > 200 for value in pixel)

time.sleep(1)
pyautogui.click(1270, 530)
time.sleep(1)

screenshot = ImageGrab.grab()
screenshot.save("screenshot.png")

white_pixels = []

for x in range(x1, x2 + 1, 10):
    for y in range(y1, y2 + 1, 10):
        for i in range(x, x + 10):
            for j in range(y, y + 10):
                pixel_color = screenshot.getpixel((i, j))
                if is_white_pixel(pixel_color):
                    white_pixels.append((i, j))
                    break

# Fai clic solo sul primo pixel bianco trovato in ciascun quadrato
for x, y in white_pixels:
    #pyautogui.click(x, y)
    False