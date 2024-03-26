import time
from PIL import ImageGrab
import pyautogui as pag
import pynput.keyboard
from pynput.keyboard import Key
from pytesseract import image_to_string
keyboard=pynput.keyboard.Controller()

def reset():
    for _ in range(3):
        # Reset until at hive and convert
        for _ in range(8):
            pag.press('esc')
            time.sleep(0.1)
            pag.press('r')
            time.sleep(0.2)
            pag.press('enter')
            time.sleep(9)

            text = image_to_string(ImageGrab.grab(bbox=(1018, 45, 1295, 100)).convert('L'))
            if 'Make Honey' in text or 'Flower Fields' in text:
                if 'Flower Fields' in text:
                    pag.press('e')
                    while 'Flower Fields' not in text:
                        time.sleep(15)
                        text = image_to_string(ImageGrab.grab(bbox=(1018, 45, 1295, 100)).convert('L'))
                break

        #Move this to checks function
        for _ in range(4):
            pix = ImageGrab.grab().getpixel((2240, 2518))[:3]
            if (abs(pix[2]-pix[1])+abs(pix[2]-pix[0])+abs(pix[1]-pix[0]))/3 < 6:
                    time.sleep(0.1)
                    for _ in range(4):
                        keyboard.press('o')
                        time.sleep(0.1)
                        keyboard.release('o')
                    return True
            for _ in range(4):
                pag.press('.')
                time.sleep(0.05)
    #call checks in order

def checkTypes(type):
    match type:
        case 0: #Slot Check
            for _ in range(2):
                for _ in range(4):
                    pag.press('.')
                    time.sleep(0.05)
                pixel = ImageGrab.grab().getpixel((2240, 2518))[:3]
                if 165<pixel[0]<184 and 118<pixel[1]<135 and 36<pixel[2]<48:
                    for _ in range(4):
                        pag.press('.')
                        time.sleep(0.05)
                    return True
                 
        case 1: #Top Check
            for _ in range(4):
                keyboard.press(Key.page_up)
                keyboard.release(Key.page_up)
                time.sleep(0.1)
            for _ in range(6):
                keyboard.press('o')
                time.sleep(0.1)
                keyboard.release('o')

            for _ in range(4):
                pixel = ImageGrab.grab().getpixel((2240, 2516))[:3]
                for _ in range(4):
                    pag.press('.')
                    time.sleep(0.05)
                if 130<pixel[0]<160 and 110<pixel[1]<140 and 40<pixel[2]<56:
                    for _ in range(4):
                        keyboard.press(Key.page_down)
                        keyboard.release(Key.page_down)
                        time.sleep(0.1)
                    return True

        case 2: #Balloon Check
            return True
        
        case 3: #Reset and Scatter Check
            return True

def hold(k, t):
    pag.keyDown(k)
    time.sleep(t)
    pag.keyUp(k)

def cannon():
    # Detect and use cannon
    hold('w', 0.8)
    pag.keyDown("d")
    time.sleep(6.5)
    hold('space', 0.08)
    time.sleep(0.2)
    pag.keyUp("d")
    hold('w', 0.15)

    #Gradual movement
    for _ in range(6):
        time.sleep(0.5)
        if 'Red Cannon' in image_to_string(ImageGrab.grab(bbox=(1130, 50, 1285, 85)).convert('L')):
            return True
        hold('d', 0.2)

    hold('s', 0.1)

    for _ in range(6):
        time.sleep(0.5)
        if 'Red Cannon' in image_to_string(ImageGrab.grab(bbox=(1130, 50, 1285, 85)).convert('L')):
            return True
        hold('a', 0.2)

    return False

def walkToRegular():
    #print('reg')
    pag.press('e')
    time.sleep(0.5)
    hold('a', 0.3)
    pag.press('space')
    pag.press('space')
    time.sleep(2.25)
    hold('s', 0.3)
    time.sleep(1)
    pag.press('space')
    hold('d', 3)
    hold('a', 0.01)
    for _ in range(7):
        if 'Memory Match' in image_to_string(ImageGrab.grab(bbox=(1020, 71, 1295, 100)).convert('L')):
            return True
        hold('w', 0.15)
        time.sleep(0.5)


def walkToMega():
    print('mega')

def walkToExtreme():
    print('Extreme')

time.sleep(3)
sucesses = {'resets':0, 'cannon':0, 'match':0}
fails = {'resets':0, 'cannon':0, 'match':0}
t = time.time()

try:
    while time.time() - t < 3600*6:
        if reset():
            sucesses['resets'] += 1
            if cannon():
                sucesses['cannon'] += 1
                if walkToRegular():
                    sucesses['match'] += 1
                else:
                    fails['match'] += 1  
            else:
                fails['cannon'] += 1
        else:
            fails['resets'] += 1
    print('Fails:', fails)
    print('Successes:', sucesses)
except:
    print('Fails:', fails)
    print('Successes:', sucesses)