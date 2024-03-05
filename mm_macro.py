import time
import memory_match
import testing
import pyautogui as pag

time.sleep(3)
collected = {}
games = {'Regular':0, 'Mega':0, 'Night':0, 'Extreme':0, 'Winter':0}

def macro(collected, times):
    for i in range(times):
        type = memory_match.initialize()

        if type:
            games[type] += 1

            if type != 'Extreme' and type != 'Winter':
                items = memory_match.play(type)
            else:
                items = memory_match.play(type, 16, (1919, 1019))

            collected = testing.identify(items, collected)
            print(collected)
        else:
            print('Not Found')

        if i != times - 1:
            for _ in range(8):
                time.sleep(15*60)
                pag.press('1')

    testing.writeSummary(collected, games)

macro(collected, 1)

# Add CD <-- This next?
# Add outside loop
# Item Summary <-- This next?
# polish stuff
# wazzup squirt