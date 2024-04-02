import time
import memory_match
import itemSummary
import goToMatch
import pyautogui as pag

def macro():
    time.sleep(3)
    t = time.time()
    t1 = time.time()
    lastType = False
    collected = {}
    cooldowns = {'Regular':0, 'Mega':0, 'Extreme':0, 'Night':0}# 'Winter':0}
    games = {'Regular':0, 'Mega':0, 'Extreme':0, 'Night':0, 'Winter':0}
    itemSummary.clearFolder()

    try:
        while True:
            t2 = time.time()
            for key in cooldowns:
                if cooldowns[key] == 0:
                    type = key

                    while True:
                        if lastType != type:
                            status, cd = goToMatch.walkToMatch(type)
                        else:
                            status, cd = goToMatch.getCD(type)

                        if status == 0:
                            continue
                        elif status == 1:
                            cooldowns[type] = cd + (time.time() - t2)
                            break
                        elif status == 2:
                            games[type] += 1
                            cooldowns[type] = cd + (time.time() - t2) # alternate: add time to type when walking to it?
                            collected = itemSummary.identify(memory_match.solve(type), collected)
                            break

                    lastType = type
                    print(cooldowns)
                    break
                    
            # Cooldown tracking system
            goToMatch.reset()
            pag.press('.')
            wait = True
            night = False
            while wait:
                for _ in range(60):
                    for key in cooldowns:
                        cooldowns[key] -= time.time() - t
                        if cooldowns[key] <= 0:
                            cooldowns[key] = 0
                            if key != 'Night' or (key == 'Night' and night):
                                wait = False
                    t = time.time()
                    if wait:
                        time.sleep(15)
                        night = goToMatch.detectNight()
                    else:
                        break
                pag.press('k')
            pag.press(',')
            print(cooldowns)

    # When macro is manually stopped write a summary.
    except KeyboardInterrupt:
        itemSummary.writeSummary(collected, games)
        print(time.time()-t1)

macro()

# Night MM
# When a MM is almost ready walk to it and wait?
# polish stuff
# ;)