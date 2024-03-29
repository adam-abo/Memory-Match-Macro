import time
import memory_match
import itemSummary
import goToMatch
import pyautogui as pag

def macro():
    time.sleep(3)
    collected = {}
    cooldowns = {'Regular':0, 'Mega':0, 'Extreme':0}#, 'Night':0, 'Winter':0}
    games = {'Regular':0, 'Mega':0, 'Extreme':0, 'Night':0, 'Winter':0}
    itemSummary.clearFolder()

    try:
        while True:
            mini = 9999
            for key in cooldowns:
                if cooldowns[key] < mini:
                    mini = cooldowns[key]
                    type = key
            if mini == 0:
                while True:
                    status, cd = goToMatch.walkToMatch(type)
                    if status == 0:
                        continue
                    elif status == 1:
                        ready = False
                        cooldowns[type] = cd
                        break
                    elif status == 2:
                        ready = True
                        cooldowns[type] = cd
                        break
            else:
                goToMatch.reset()
                wait = True
                while wait:
                    pag.press('k')
                    time.sleep(300)
                    for key in cooldowns:
                        cooldowns[key] -= 300
                        if cooldowns[key] <= 0:
                            cooldowns[key] = 0
                            wait = False

            if ready:
                ready = False
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
            print(cooldowns)

    except KeyboardInterrupt:
        itemSummary.writeSummary(collected, games)

macro()

# Add CD <-- This next?
# Add outside loop
# polish stuff
# ;)