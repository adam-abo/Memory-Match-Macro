import time
from PIL import ImageGrab
import pyautogui as pag
import pynput.keyboard
from pynput.keyboard import Key
from pynput.mouse import Button, Controller
from pytesseract import image_to_string
mouse = Controller()
keyboard = pynput.keyboard.Controller()
import random

# Not being used currently
'''
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
'''
def oriented():
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
    return False

def reset():
    for _ in range(3):
        # Reset until at hive and convert
        for _ in range(8):
            pag.press('esc')
            time.sleep(0.1)
            pag.press('r')
            time.sleep(0.2)
            pag.press('enter')
            time.sleep(8.5)

            text = image_to_string(ImageGrab.grab(bbox=(1018, 45, 1295, 100)).convert('L'))
            if 'Make Honey' in text or 'rom Flower' in text:
                if 'Make Honey' in text:
                    pag.press('e')
                    while 'rom Flower' not in text:
                        time.sleep(3)
                        text = image_to_string(ImageGrab.grab(bbox=(1018, 45, 1295, 100)).convert('L'))
                    time.sleep(3)
                break

        if oriented():
            break
    return True

def hold(k, t):
    if k == 'space':
        k = Key.space
    keyboard.press(k)
    time.sleep(t)
    keyboard.release(k)

def multiHold(k, t):
    for c in k:
        keyboard.press(c)
    time.sleep(t)
    for c in k:
        keyboard.release(c)

def jump(k='', t=0):
    for c in k:
        keyboard.press(c)
    hold('space', 0.08)
    time.sleep(t)
    for c in k:
        keyboard.release(c)


def cannon(slot):
    # Detect and use cannon
    hold('w', 0.7)
    pag.keyDown("d")
    time.sleep(1.2*slot)
    jump()
    time.sleep(0.2)
    pag.keyUp("d")
    hold('w', 0.25)

    #Gradual movement
    for _ in range(6):
        time.sleep(0.5)
        if 'Red Cannon' in image_to_string(ImageGrab.grab(bbox=(1130, 50, 1285, 85)).convert('L')):
            return True
        hold('d', 0.2)

    hold('s', 0.2)

    for _ in range(6):
        time.sleep(0.5)
        if 'Red Cannon' in image_to_string(ImageGrab.grab(bbox=(1130, 50, 1285, 85)).convert('L')):
            return True
        hold('a', 0.2)

    return False

def detectNight():
    pag.press('.')
    img = ImageGrab.grab(bbox=(2160,0,2240,80)).convert('L')
    time.sleep(0.1)
    pag.press(',')
    width, height = img.size
    black_pixels = 0

    for y in range(height):
        for x in range(width):
            pixel_value = img.getpixel((x, y))
            if pixel_value == 0:
                black_pixels += 1

    del img
    if black_pixels/(width * height) > 0.9:
        return True
    return False

def walkToMatch(type, slot):
    reset()
    if type == 'Night' and not detectNight():
        return 0, 1

    if cannon(slot):
        match type:
            case 'Regular':
                return walkToRegular()
            case 'Mega':
                return walkToMega()
            case 'Extreme':
                return walkToExtreme()
            case 'Night':
                return walkToNight()
    return 0, 0

def walkToRegular():
    pag.press('e')
    time.sleep(0.5)
    hold('a', 0.5)
    pag.press('space')
    pag.press('space')
    time.sleep(2.5)
    hold('s', 0.5)
    time.sleep(1)
    pag.press('space')
    hold('d', 2)
    hold('a', 0.2)
    for _ in range(7):
        if 'PlayMemoryMatch' in image_to_string(ImageGrab.grab(bbox=(955, 40, 1295, 100)).convert('L')).replace(" ", "").replace("\n", ""):
            time.sleep(0.5)
            text = image_to_string(ImageGrab.grab(bbox=(955, 40, 1295, 100)).convert('L')).replace(" ", "").replace("\n", "")
            if 'PlayMemoryMatch' in text:
                return getCD('Regular')
        hold('w', 0.25)
        time.sleep(0.5)
    ImageGrab.grab().save("/XXX/Regular"+str(random.randint(0,10000))+".png") # Replace XXX with desired directory
    return 0, 0

def walkToMega():
    pag.press('e')
    time.sleep(0.8)
    hold('d', 0.5)
    pag.press('space')
    pag.press('space')
    time.sleep(5.15)
    pag.press('space')
    time.sleep(2)
    hold('s', 0.5)
    hold('w', 3)
    hold('s', 0.2)
    for _ in range(8):
        if 'Mega' in image_to_string(ImageGrab.grab(bbox=(955, 40, 1295, 100)).convert('L')):
            time.sleep(0.5)
            text = image_to_string(ImageGrab.grab(bbox=(955, 40, 1295, 100)).convert('L'))
            if 'Mega' in text:
                return getCD('Mega')
        hold('d', 0.25)
        time.sleep(0.5)
    ImageGrab.grab().save("/XXX/Mega"+str(random.randint(0,10000))+".png") # Replace XXX with desired directory
    return 0, 0

def walkToExtreme():
    hold('d', 3)
    hold('w', 1)
    hold('a', 0.08)
    jump()
    hold('d', 2.5)
    jump()
    keyboard.press('w')
    time.sleep(2.5)
    hold('space', 1.5)
    hold('d', 0.7)
    time.sleep(1.3)
    jump()
    time.sleep(4)
    jump()
    time.sleep(0.75)
    keyboard.release('w')
    for _ in range(8):
        if 'Extreme' in image_to_string(ImageGrab.grab(bbox=(955, 40, 1295, 100)).convert('L')):
            time.sleep(0.5)
            text = image_to_string(ImageGrab.grab(bbox=(955, 40, 1295, 100)).convert('L'))
            if 'Extreme' in text:
                return getCD('Extreme')
        hold('d', 0.25)
        time.sleep(0.5)
    ImageGrab.grab().save("/XXX/Extreme"+str(random.randint(0,10000))+".png") # Replace XXX with desired directory
    return 0, 0

def walkToNight():
    #Check if dead (when dead check if still night)
    pag.press('e')
    time.sleep(2.5)
    hold('s', 2.5)
    hold('d', 2)
    hold('a', 0.3)
    hold('s', 0.5)
    hold('a', 1.5)
    hold('s', 3)
    for _ in range(60):
        hold('s', 0.05)
        time.sleep(0.05)
    multiHold('sa', 4)
    hold('a', 0.25)
    pag.press(',')
    
    # Moon Jumps
    jump('w', 1)
    jump('w', 0.95)
    pag.press('.')
    jump('w', 0.7)# here
    multiHold('aw', 0.25)
    hold('w', 0.1)
    jump('w', 1)
    pag.press('.')
    hold('w', 0.2)
    pag.press(',')
    jump('w', 0.6)
    pag.press('.')
    hold('w', 0.5)
    keyboard.press('w')
    jump('a', 0.3)
    time.sleep(0.5)
    keyboard.release('w')
    jump('w', 0.8)
    hold('d', 0.2)
    jump('w', 0.8)
    pag.press('.')
    hold('w', 0.3)
    hold('d', 0.2)
    keyboard.press('w')
    jump('d', 0.3)
    time.sleep(0.5)
    keyboard.release('w')
    multiHold('aw', 3)
    hold('d', 1)
    multiHold('dw', 0.4)
    hold('w', 1.4)
    multiHold('aw', 0.4)
    hold('a', 1)
    multiHold('as', 1)
    multiHold('dw', 0.3)
    for _ in range(7):
        if 'Night' in image_to_string(ImageGrab.grab(bbox=(955, 40, 1295, 100)).convert('L')).replace(" ", "").replace("\n", ""):
            time.sleep(0.5)
            text = image_to_string(ImageGrab.grab(bbox=(955, 40, 1295, 100)).convert('L')).replace(" ", "").replace("\n", "")
            if 'Night' in text:
                return getCD('Night')
        hold('w', 0.25)
        time.sleep(0.5)
    ImageGrab.grab().save("/XXX/Night"+str(random.randint(0,10000))+".png") # Replace XXX with desired directory
    return 0, 0

def getCD(type):
    defaults = {'Regular':7200, 'Mega':14400, 'Extreme':28800, 'Night':28800, 'Winter':28800}
    text = image_to_string(ImageGrab.grab(bbox=(955, 40, 1295, 100)).convert('L'))

    if '(' in text and ')' in text:
        text = text.replace(':','').replace('s','')     
        text = text[text.index(')')-1:text.index('('):-1]
        secs = 0
        multi = 1

        for n in range(len(text)):
            secs += int(text[n]) * multi
            if n % 2:
                multi = multi*6
            else:
                multi = multi*10
        if secs < defaults[type]:
            #ImageGrab.grab().save("/XXX/CD"+str(random.randint(0,10000))+".png")
            return 1, secs
    return 2, defaults[type]

def hiveSlot():
    for _ in range(4):
        reset()
        hold('w', 0.7)
        hold('d', 7.4)
        hold('s', 0.5)
        hold('a', 0.5)
        time.sleep(0.5)

        for slot in range(6):
            text = image_to_string(ImageGrab.grab(bbox=(1018, 45, 1295, 100)).convert('L'))
            if 'Make Honey' in text or 'rom Flower' in text:
                return slot + 1
            elif slot == 5:
                break
            else:
                print(text)
            hold('a', 1.3)
            time.sleep(0.5)
    return 6

def claimHive():
    for _ in range(15):
        hold('w', 2.75)
        hold('d', 3.7)
        hold('s', 0.5)
        hold('a', 0.5)
        time.sleep(0.3)

        for slot in range(6):
            text = image_to_string(ImageGrab.grab(bbox=(1018, 45, 1295, 100)).convert('L'))
            if 'Claim Hive' in text:
                pag.press('e')
                return slot + 1
            elif slot == 5:
                break
            hold('a', 1.3)
            time.sleep(0.3)

        reset()
    exit()

def checkReconnect():
    if ImageGrab.grab(bbox=(1100, 570, 1101, 571)).getpixel((0,0))[:3] == (57,59,61):
        print('Disconnected')
        if 'Reconnect' in image_to_string(ImageGrab.grab(bbox=(1175, 710, 1250, 725)).convert('L')):
            print('Clicked Reconnect')
            mouse.position = (1200, 715)
            time.sleep(0.1)
            mouse.click(Button.left, 1)
        else:
            print('Reconnect Not Found')
            exit()

        time.sleep(10)
        waitTime = 5
        while ImageGrab.grab(bbox=(1100, 570, 1101, 571)).getpixel((0,0))[:3] == (57,59,61):
            time.sleep(waitTime)
            print('Current Wait Time:', waitTime)
            waitTime*2
        
        print('Loading')

        waitTime = 10
        while (200,80,75) <= ImageGrab.grab(bbox=(2215, 155, 2216, 156)).getpixel((0,0))[:3] <= (205,87,80):
            print(ImageGrab.grab(bbox=(2145, 115, 2146, 116)).getpixel((0,0))[:3])
            time.sleep(waitTime)
            print('Current Wait Time:', waitTime)
            waitTime*2

        print('Rejoined Successfully')
        return True
    return False

"""time.sleep(2)
reset()
trials = 0
sucesses = 0
try:
    while True:
        if detectNight():
            trials += 1
            if walkToMatch('Night', 4) == 1:
                sucesses +=1
            reset()
            time.sleep(1000)
        time.sleep(10)
except KeyboardInterrupt:
    print(trials, sucesses)"""
