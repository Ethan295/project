import pyautogui
import time
from array import array


time.sleep(1)

white_found = 0

number_found_1_1 = array('i', [])
number_found_1_2 = array('i', [])
number_found_1_3 = array('i', [])
number_found_2_1 = array('i', [])
number_found_2_2 = array('i', [])
number_found_2_3 = array('i', [])
number_found_3_1 = array('i', [])
number_found_3_2 = array('i', [])
number_found_3_3 = array('i', [])

positions_to_click = [] 


round = 0

pyautogui.click(1270, 530)
for i in range(0, 11):
    
    
    positions_to_click = [] 
    time.sleep(0.1)
    while not white_found == round:
        pixel_color_1_1 = pyautogui.pixel(1140, 300)
        pixel_color_1_2 = pyautogui.pixel(1270, 300)
        pixel_color_1_3 = pyautogui.pixel(1400, 300)
        pixel_color_2_1 = pyautogui.pixel(1140, 430)
        pixel_color_2_2 = pyautogui.pixel(1270, 430)
        pixel_color_2_3 = pyautogui.pixel(1400, 430)
        pixel_color_3_1 = pyautogui.pixel(1140, 560)
        pixel_color_3_2 = pyautogui.pixel(1270, 560)
        pixel_color_3_3 = pyautogui.pixel(1400, 560)

        if pixel_color_1_1 > (200, 200, 200):
            white_found += 1
            positions_to_click.append((1140, 300))
            time.sleep(0.4)
        elif pixel_color_1_2 > (200, 200, 200):
            white_found += 1
            positions_to_click.append((1270, 300))
            time.sleep(0.4)
        elif pixel_color_1_3 > (200, 200, 200):
            white_found += 1
            positions_to_click.append((1400, 300))
            time.sleep(0.4)
        elif pixel_color_2_1 > (200, 200, 200):
            white_found += 1
            positions_to_click.append((1140, 430))
            time.sleep(0.4)
        elif pixel_color_2_2 > (200, 200, 200):
            white_found += 1
            positions_to_click.append((1270, 430))
            time.sleep(0.4)
        elif pixel_color_2_3 > (200, 200, 200):
            white_found += 1
            positions_to_click.append((1400, 430))
            time.sleep(0.4)
        elif pixel_color_3_1 > (200, 200, 200):
            white_found += 1
            positions_to_click.append((1140, 560))
            time.sleep(0.4)
        elif pixel_color_3_2 > (200, 200, 200):
            white_found += 1
            positions_to_click.append((1270, 560))
            time.sleep(0.4)
        elif pixel_color_3_3 > (200, 200, 200):
            white_found += 1
            positions_to_click.append((1400, 560))
            time.sleep(0.4)
        
    
    time.sleep(1)

    white_found = 0
    for x, y in positions_to_click:
        pyautogui.click(x, y)
        time.sleep(0.2)

        #print(str(x) + " " + str(y) + " cliccato")
        #print("posizione: " + str(positions_to_click))

    round += 1

"""
print(number_found_1_1)
print(number_found_1_2)
print(number_found_1_3)
print(number_found_2_1)
print(number_found_2_2)
print(number_found_2_3)
print(number_found_3_1)
print(number_found_3_2)
print(number_found_3_3)
"""