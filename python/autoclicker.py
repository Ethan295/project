import pyautogui
import appJar
import keyboard

def buttonPress(btn):
    if btn == 'Start(s)' or keyboard.is_pressed('s'):
        amount = app.getEntry('amount')
        btn = app.getRadioButton('click')
        if btn == 'right button':
            btn = 'right'
        else:
            btn = 'left'
        for _ in range(int(amount)):
            pyautogui.click(button=btn)

app = appJar.gui('autoClicker')
app.setSize(300, 200)
app.setSticky('news')
app.addLabel('title', 'Auto Clicker')
app.addEntry('amount')
app.addButton('Start(s)', buttonPress, row=3)
app.setSticky('e')
app.radioButton('click', 'right button', row=2)
app.setSticky('w')
app.radioButton('click', 'left button', row=2)

app.go()
