import time
import memory_match
import testing
import pyautogui as pag

time.sleep(3)
collected = {}

for i in range(4):
    type = memory_match.initialize()
    if type:
        if type > 2:
            items = memory_match.play(type)
        else:
            items = memory_match.play(type, 16, (1919, 1019))

        collected = testing.identify(items, collected)
        print(collected)
    else:
        print('Not Found')

    if i != 3:
        for _ in range(8):
            time.sleep(15*60)
            pag.press('1')

# Add CD <-- This next?
# Add outside loop
# Item Summary <-- This next?
# polish stuff
# Ayo lil' bro