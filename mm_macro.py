import time
import memory_match
import testing
import pyautogui as pag

collected = {}
current_collected = {}
time.sleep(3)

for i in range(4):
    type = memory_match.initialize()
    if type:
        if type > 2:
            items = memory_match.play(type)
        else:
            items = memory_match.play(type, 16, (1919, 1019))

        current_collected = testing.identify(items, current_collected)
        print(current_collected)
        for item in current_collected:
            if item[:3] in collected:
                collected[item[:3]] += item[3]
            else:
                collected[item[:3]] = item[3]
    else:
        print('Not Found')

    if i != 3:
        for _ in range(8):
            time.sleep(15*60)
            pag.press('1')

print(collected)

# Add CD <-- This next?
# Add outside loop
# Item Summary <-- This next?
# polish stuff
# Ayo lil' bro