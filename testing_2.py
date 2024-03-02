import testing
import pyautogui as pag
import time

def hallo():
    known_items = testing.identify()
    collected = {}
    board = [(207, 73, 67, 3), ]

    for item in board:
        if item[4] == 1:
            quantity = item[3]
            item = item[:3]

            if str(item) in known_items and item not in collected:
                item = known_items[str(item)]
                if item in collected:
                    collected[item] += quantity
                else:
                    collected[item] = 0
            else:
                collected[item] = 0
    print(collected)

time.sleep(3)
for _ in range(2):
    pag.press('d')
pag.press('enter')