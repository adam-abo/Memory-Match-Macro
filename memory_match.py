import time
import os
import pyautogui as pag
from PIL import ImageGrab
import random
from pytesseract import image_to_string

def clickTile(tile, clickPos):
    time.sleep(1)
    pag.leftClick(clickPos[0] + (tile // 4) * 80, y = clickPos[1] + (tile % 4) * 80)

def beginMatch(tiles, currentTile, chances, clickPos):
    foundTile = tiles.index(tiles[currentTile])

    tiles[currentTile] = tiles[currentTile][:4] + (True,)
    tiles[foundTile] = tiles[foundTile][:4] + (True,)

    if chances % 2 == 1:
        chances -= 1
        clickTile(foundTile, clickPos)
    else:
        chances -= 2
        clickTile(currentTile, clickPos)
        clickTile(foundTile, clickPos)
    return chances

def recognize(currentTile, initialPos):
    t = time.time()
    x = initialPos[0] + (currentTile // 4) * 160
    y = initialPos[1] + (currentTile % 4) * 160
    scaled_x = x // 2
    scaled_y = y // 2
    attempt = 7

    while (ImageGrab.grab(bbox=(scaled_x, scaled_y, scaled_x+1, scaled_y+1))).getpixel((0,0))[:3] == (170, 130, 73):
        if (time.time() - t) > attempt:
            print('Attemt #' + str(attempt/7 + 1) + ' of flipping tile ' + str(currentTile))
            pag.leftClick()
            attempt += 7
        elif time.time() - t > 17:
            print('Error: tile ' + str(currentTile) + ' has not flipped')
            exit()

    time.sleep(0.15) 
    img = ImageGrab.grab()
    ###
    if 130 < img.getpixel((x, y))[0] < 140:
        r = random.randint(0,10000)
        img.save("/Users/adamabouelela/Desktop/mi"+str(r)+".png")
    ###
    return img.getpixel((x, y))[:3] + (quantify(img.crop((x-35, y+15, x+50, y+50))), False)

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
    
def itemsMatched(items):
    matches = []
    for item in items:
        if item[4]:
            matches.append(item[:4])      
    matches.sort()
    matches = matches[::2]
    
    for item in matches:
        if matches.count(item) == 2:
            matches.remove(item)
            matches[matches.index(item)] = item[:3] + (item[3]*2,)
            break
    print(matches)
    return matches

def save_board(initialPos, final_pix):
    t = time.time()
    scaled_x = (initialPos[0] + 480 + final_pix) // 2
    scaled_y = (initialPos[1] + 480) // 2
    while ImageGrab.grab(bbox=(scaled_x, scaled_y, scaled_x+1, scaled_y+1)).getpixel((0,0))[:3] == (170, 130, 73):
        if time.time() - t > 7:
            print('Game was thought to end.')
            exit()

    time.sleep(0.1)
    img = ImageGrab.grab().crop((1600, 850, 2700, 1650))
    counter = 1
    name = 'board'
    nameC = f"{name}_{counter}"
    path = "/Users/adamabouelela/Desktop/Memory-Match-Macro/Boards/"

    while os.path.exists(os.path.join(path, nameC + '.png')):
        nameC = f"{name}_{counter}"
        counter += 1
    img.save(path + nameC + '.png')

def solve(type):
    currentTile = 0
    tiles = []
    dupes = []

    if type != 'Extreme' and type != 'Winter':
        chances = 12
        final_pix = 0
        initialPos = (1999, 1019)
        clickPos = (970, 535)
        if type == 'Night':
            dupePot = (58, 57, 56)
        else:
            dupePot = (136, 99, 163)
    else:
        chances = 16
        final_pix = 16 * 40
        initialPos = (1919, 1019)
        clickPos = (930, 535)
        dupePot = (136, 99, 163)

    try:
        t = time.time()
        while ImageGrab.grab(bbox=(initialPos[0], initialPos[1], initialPos[0]+1, initialPos[1]+1)).getpixel((0,0))[:3] == (170, 130, 73):
            if time.time() - t > 7:
                print('Game has not started.')
                exit()

        pag.press('e')
        time.sleep(5) # replace this to check wheter it can see the tile color

        while 0 < chances:
            # Checks to see if it isn't the last turn to match possible duplicate pairs. It will not match a dupe pair if it finds a different pair to match at the last moment.
            if len(dupes) < 2 or chances != 2:
                chances -= 1
                clickTile(currentTile, clickPos)
                currentImage = recognize(currentTile, initialPos)
                tiles.append(currentImage)
            else:
                tiles[dupes[0]] = tiles[dupes[0]][:4] + (True,)
                tiles[dupes[1]] = tiles[dupes[1]][:4] + (True,)
                clickTile(dupes[1], clickPos)
                clickTile(dupes[0], clickPos)
                break
            
            if currentImage == tiles[currentTile-1] and chances % 2 == 0:
                tiles[currentTile] = tiles[currentTile][:4] + (True,)
                tiles[currentTile-1] = tiles[currentTile-1][:4] + (True,)
                if currentImage[:3] == dupePot:
                    dupes = []
                    dupePot = False

            elif currentImage[:3] == dupePot and chances > 2:
                    dupes.append(currentTile)
                    if len(dupes) == 3 or (len(dupes) == 2 and chances % 2 == 1):
                        chances = beginMatch(tiles, currentTile, chances, clickPos)
                        dupes = []
                        dupePot = False

            elif currentImage in tiles[:currentTile] and chances > 0:
                chances = beginMatch(tiles, currentTile, chances, clickPos)

            currentTile += 1

        print(tiles)
        save_board(initialPos, final_pix)
        return itemsMatched(tiles)
    
    except SystemExit:
        print('holding game open for ma lord')
        for _ in range(100):
            time.sleep(15*60)
            pag.press('k')