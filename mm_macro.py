import time
import memory_match
import itemSummary
import goToMatch
import pyautogui as pag

def macro():
    time.sleep(3)
    collected = {}
    there = False
    games = {'Regular':0, 'Mega':0, 'Night':0, 'Extreme':0, 'Winter':0}
    itemSummary.clearFolder()

    try:
        while True:
            type, cd, ready = memory_match.initialize()

            if type:
                if ready:
                    games[type] += 1

                    try:
                        if type != 'Extreme' and type != 'Winter':
                            items = memory_match.play(type)
                        else:
                            items = memory_match.play(type, 16, (1919, 1019), (930, 535))
                        collected = itemSummary.identify(items, collected)
                        print(collected)

                    except SystemExit:
                        print('holding game open for ma lord')
                        for _ in range(100):
                            time.sleep(15*60)
                            pag.press('k')
            else:
                print('Not Found')
                
                for _ in range(cd):
                    time.sleep(15*60)
                    pag.press('k')

                while not there:
                    if goToMatch.reset():
                        if goToMatch.cannon():
                            if goToMatch.walkToRegular():
                                there = True

    except KeyboardInterrupt:
        itemSummary.writeSummary(collected, games)

macro()

# Add CD <-- This next?
# Add outside loop
# polish stuff
# ;)