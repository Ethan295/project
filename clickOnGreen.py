
import pyautogui
from PIL import Image
import time

#pygame.init() # inizzializza



screen_width, screen_height = 800, 600  # Crea una finestra per la visualizzazione:
#screen = pygame.display.set_mode((screen_width, screen_height))


screen_width, screen_height = pyautogui.size()



# pygame.display.update() nel for per veder cosa fa

screen_width, screen_height = pyautogui.size() # ottieni dimensioni schermo

screenshot = pyautogui.screenshot() # screanshot intero schermo

box_x, box_y = 1060, 210
square_size = 420# Dimensioni del riquadro (larghezza e altezza)


box_image = screenshot.crop((box_x, box_y, box_x + square_size, box_y + square_size)) # Ritaglia il riquadro dall'immagine dello schermo



box_image.show()

desired_color = (75, 219, 106)


while True:
    # Cattura uno screenshot dell'intero schermo
    screenshot = pyautogui.screenshot()

    # Ritaglia il riquadro dall'immagine dello schermo
    box_image = screenshot.crop((box_x, box_y, box_x + square_size, box_y + square_size))

    is_color_found = False

    for x in range(square_size):
        for y in range(square_size):
            pixel_color = box_image.getpixel((x, y))
            if pixel_color == desired_color:
                pyautogui.click(400, 300)
                break



        
    # Aggiungi un ritardo tra le iterazioni del loop (ad esempio, 1 secondo)
    #time.sleep(1)

    # Controllo eventi Pygame per verificare la chiusura della finestra (opzionale)
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    """
  