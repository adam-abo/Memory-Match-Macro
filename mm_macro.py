import time
import memory_match
import itemSummary
import moveDetect
import pyautogui as pag

def macro():
    time.sleep(3)
    collected = {}
    cooldowns = {'Regular':0, 'Mega':0, 'Extreme':0, 'Night':0}# 'Winter':0}
    games = {'Regular':0, 'Mega':0, 'Extreme':0, 'Night':0, 'Winter':0}
    itemSummary.clearFolder()
    t = t1 = time.time()
    slot = moveDetect.hiveSlot()

    try:
        while True:
            for key in cooldowns:
                # Attempt to play when the type's cooldown = 0
                if cooldowns[key] == 0:
                    print(key)
                    while True:
                        status, cd = moveDetect.walkToMatch(key, slot)
                        if status == 0:
                            if key == 'Night' and cd:
                                break
                            elif moveDetect.checkReconnect():
                                slot = moveDetect.claimHive()
                        elif status == 1:
                            cooldowns[key] = cd + (time.time() - t)
                            break
                        elif status == 2:
                            games[key] += 1
                            cooldowns[key] = cd + (time.time() - t) # alternate: add time to type when walking to it?
                            collected = itemSummary.identify(memory_match.solve(key), collected)
                            break
                    print(cooldowns)
                    break
                    
            # Cooldown tracking system
            if min(cooldowns, key=cooldowns.get) == 'Night':
                moveDetect.reset()
            wait = True
            while wait:
                for _ in range(60):
                    for key in cooldowns:
                        cooldowns[key] -= time.time() - t
                        if cooldowns[key] <= 0:
                            cooldowns[key] = 0
                            if wait and (key != 'Night' or moveDetect.detectNight()):
                                wait = False
                    t = time.time()
                    if wait:
                        time.sleep(15)
                    else:
                        break
                pag.press('k')
                if moveDetect.checkReconnect():
                    slot = moveDetect.claimHive()
                    moveDetect.reset()
            print(cooldowns)

    # When macro is manually stopped write a summary.
    except KeyboardInterrupt:
        itemSummary.writeSummary(collected, games)
        print(time.time()-t1)

macro()

# When a MM is almost ready walk to it and wait? (look for night when Night MM is close)
# polish stuff
# 3:O