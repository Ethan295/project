import pyautogui
import time

# Funzione per verificare se un pixel è simile al bianco
def is_similar_to_white(pixel_color, tolerance=20):
    r, g, b = pixel_color
    return r > 255 - tolerance and g > 255 - tolerance and b > 255 - tolerance

def is_box_white(coords):
    for x, y in coords:
        pixel_color = pyautogui.pixel(x, y)
        if is_similar_to_white(pixel_color):
            return True, (x, y)
    return False, None

def main():
    boxes_coords = [
        (1082, 239), (1215, 239), (1348, 239),
        (1082, 373), (1215, 373), (1348, 373),
        (1082, 505), (1215, 505), (1348, 505)
    ]

    white_boxes = set()

    while True:
        box_white, box_coords = is_box_white(boxes_coords)
        if box_white and box_coords not in white_boxes:
            white_boxes.add(box_coords)
            print(f"Il box diventa bianco: {box_coords}")

          # Ritardo di 2 secondi tra ogni controllo

if __name__ == "__main__":
    main()



    #è impossibile mi sono arreso 
