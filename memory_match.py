# Main Gameplay Loop (pixel matching and tile movement)

import time
import pyautogui as pag
from PIL import ImageGrab
from pytesseract import image_to_string

def initialize():
    text = image_to_string(ImageGrab.grab(bbox=(1020, 71, 1295, 100)).convert('L'))
    if 'Memory Match' in text:
               
        pag.press('e')
        time.sleep(2.5)
        pag.press('\\')
        pag.press('a')
        pag.press('a')
        pag.press('s')

        if 'Extreme' in text:
            return 1
        elif 'Winter' in text:
            return 2
        elif 'Mega' in text:
            return 3
        elif 'Night' in text:
            return 4
        else:
            return 5
    else:
        return 0

def nextTile(currentTile):
    if currentTile != 0:
        if currentTile % 4 != 0:
            pag.press('s')
        else:
            for _ in range(3):
                pag.press('w')
            pag.press('d')
    pag.press('enter')
    return currentTile

def beginMatch(tiles, currentTile, chances):
    foundTile = tiles.index(tiles[currentTile])

    tiles[currentTile][4] = 1
    tiles[foundTile][4] = 1

    if chances % 2 == 1:
        chances -= 1
        matchTiles(foundTile, currentTile, chances)

    elif currentTile - foundTile != 1:
        chances -= 2
        pag.press('enter')
        matchTiles(foundTile, currentTile, chances)
    return chances

def matchTiles(index1, index2, chances):
    columns = index2 // 4 - index1 // 4
    rows = index2 % 4 - index1 % 4

    time.sleep(0.1)
    for _ in range(columns):
        pag.press('a')
    for _ in range(abs(rows)):
        if rows > 0:
            pag.press('w')
        else:
            pag.press('s')
    pag.press('enter')

    if chances > 0:
        time.sleep(0.2)
        for _ in range(abs(rows)):
            if rows > 0:
                pag.press('s')
            else:
                pag.press('w')
        for _ in range(columns):
            pag.press('d')

def matchDupe(index1, index2, currentTile):
    columns = currentTile // 4 - index2 // 4
    rows = currentTile % 4 - index2 % 4

    for _ in range(columns):
        pag.press('a')
    for _ in range(abs(rows)):
        if rows > 0:
            pag.press('w')
        else:
            pag.press('s')
    pag.press('enter')

    matchTiles(index1, index2, 0)

def recognize(currentTile, initialPos):
    t = time.time()
    x = initialPos[0] + (currentTile // 4) * 160
    y = initialPos[1] + (currentTile % 4) * 160
    scaled_x = x // 2
    scaled_y = y // 2

    while (ImageGrab.grab(bbox=(scaled_x, scaled_y, scaled_x+1, scaled_y+1))).getpixel((0,0))[:3] == (170, 130, 73):
        if time.time() - t > 7:
            print('Error: tile ' + currentTile+1 + ' has not flipped')
            exit()

    time.sleep(0.15) 
    img = ImageGrab.grab()
    return img.getpixel((x, y))[:3] + (quantify(img.crop((x-35, y+15, x+50, y+50))), 0)

def quantify(img):
    for x in range(85):
        for y in range(35):
            r, g, b = img.getpixel((x, y))[:3]
            if r != 254 or g != 250 or b != 234:
                img.putpixel((x, y), (0, 0, 0))

    text = image_to_string(img).replace('\n', '')
    if len(text) > 0:
        return int(text[text.find('x') + 1:])
    else:
        return 1

def play(type, chances = 12, initialPos = (1999, 1019)):
    currentTile = 0
    final_pix = (chances - 12) * 40
    tiles = []
    dupes = []
    if type == 4:
        dupePot = ((58, 57, 56))
    else:
        dupePot = ((136, 99, 163))

    while 0 < chances:
        # Checks to see if it isn't the last turn to match possible duplicate pairs. It will not match a dupe pair if it finds a different pair to match at the last moment.
        if len(dupes) < 2 or chances != 2:
            chances -= 1
            nextTile(currentTile)
            currentImage = recognize(currentTile, initialPos)
            tiles.append(currentImage)
        else:
            tiles[dupes[0]] = 'Match' + str(tiles[dupes[0]])
            tiles[dupes[1]] = 'Match' + str(tiles[dupes[1]])
            matchDupe(dupes[0], dupes[1], currentTile-1)
            break
        
        if currentImage[:3] == dupePot and chances > 2:
                dupes.append(currentTile)
                if len(dupes) == 3 or (len(dupes) == 2 and chances % 2 == 1):
                    chances = beginMatch(tiles, currentTile, chances)
                    dupes = []
                    dupePot = False
        elif currentImage in tiles[:currentTile] and chances > 0:
            chances = beginMatch(tiles, currentTile, chances)
        currentTile += 1

    t = time.time()
    scaled_x = (initialPos[0] + 480 + final_pix) // 2
    scaled_y = (initialPos[1] + 480) // 2
    while ImageGrab.grab(bbox=(scaled_x, scaled_y, scaled_x+1, scaled_y+1)).getpixel((0,0))[:3] == (170, 130, 73):
        if time.time() - t > 7:
            exit()

    time.sleep(0.1)
    img = ImageGrab.grab()
    img.save("/Users/adamabouelela/Desktop/final_board.png")
    pag.press('\\')
    print(dupes)
    return(tiles)