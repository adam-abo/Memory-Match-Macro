import time
import memory_match
import itemSummary
import goToMatch
import pyautogui as pag

def macro():
    time.sleep(3)
    t1 = time.time()
    lastType = False
    collected = {}
    cooldowns = {'Regular':0, 'Mega':0, 'Extreme':0}#, 'Night':0, 'Winter':0}
    games = {'Regular':0, 'Mega':0, 'Extreme':0, 'Night':0, 'Winter':0}
    itemSummary.clearFolder()

    try:
        while True:
            for key in cooldowns:
                if cooldowns[key] == 0:
                    t = time.time()
                    type = key

                    while True:
                        t2 = time.time()
                        if lastType != type:
                            status, cd = goToMatch.walkToMatch(type)
                        else:
                            status, cd = goToMatch.getCD(type)

                        if status == 0:
                            continue
                        elif status == 1:
                            cooldowns[type] = cd
                            break
                        elif status == 2:
                            games[type] += 1
                            cooldowns[type] = cd + time.time() - t2
                            collected = itemSummary.identify(memory_match.solve(type), collected)
                            break

                    for key in cooldowns:
                        if key != type:
                            cooldowns[key] -= time.time() - t
                            if cooldowns[key] < 0:
                                cooldowns[key] = 0
                    lastType = type
                    
            print(cooldowns)
            #goToMatch.reset() #If you want to put smthn in between matches
            wait = True
            while wait:
                t = time.time()
                for key in cooldowns:
                    cooldowns[key] -= time.time() - t
                    if cooldowns[key] <= 0:
                        cooldowns[key] = 0
                        wait = False
                if wait:
                    pag.press('k')
                    time.sleep(60)
            print(cooldowns)

    except KeyboardInterrupt:
        itemSummary.writeSummary(collected, games)
        print(time.time()-t1)

macro()

# Night MM
# When a MM is almost ready walk to it and wait?
# polish stuff
# ;)