import time
from PIL import ImageGrab
import pyautogui as pag
import pynput.keyboard
from pynput.keyboard import Key
keyboard=pynput.keyboard.Controller()

def reset():
    # Reset
    pag.press('esc')
    time.sleep(0.5)
    pag.press('r')
    time.sleep(0.5)
    pag.press('enter')
    time.sleep(10)

    # Adjust camera orientation
    keyboard.press(Key.page_up)
    keyboard.release(Key.page_up)
    pag.press('o', 5)
    for _ in range(4):
        img = ImageGrab.grab()
        pixel = img.getpixel((2240, 2518))[:3]
        if pixel[0] == pixel[1] == pixel[2]:
            pag.press('.', 4)
            pag.press('pgdn', 4)
        else:
            pag.press('.', 4)
            img = ImageGrab.grab()
            pixel = img.getpixel((2240, 2518))[:3]
            if pixel[0] == pixel[1] == pixel[2]:
                pag.press('.', 4)
                pag.press('pgdn', 4)

def useCannon():
    # Detect and use cannon
    pag.keyDown('d')
    time.sleep(5)
    pag.keyUp('d')
    pag.keyDown('w')
    time.sleep(1)
    pag.keyUp('w')
    pag.keyDown('d')
    pag.press('space')
    time.sleep(0.3)
    pag.keyUp('d')

    #Gradual movement
    pag.keyDown('d')
    time.sleep(0.05)
    pag.keyUp('d')

    pag.press('e')

def walkToRegular():
    print('reg')

def walkToMega():
    print('mega')

def walkToExtreme():
    print('Extreme')

#time.sleep(3)
#reset()
#useCannon()