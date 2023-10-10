import pyautogui
import os

# Take a screenshot of the region between (850, 200) and (1750, 600)
screenshot = pyautogui.screenshot(region=(850, 200, 900, 400))

# Check if the "bersaglio.png" image is present in the screenshot
if pyautogui.locateOnScreen('bersaglio.png', region=(0, 0, 900, 400), grayscale=True, confidence=0.8) is not None:
    # Click on the center of the "bersaglio.png" image
    target_location = pyautogui.locateCenterOnScreen('bersaglio.png', region=(0, 0, 900, 400), grayscale=True, confidence=0.8)
    pyautogui.click(target_location)

# Delete the screenshot file
os.remove(screenshot.filename)
