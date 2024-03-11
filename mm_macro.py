import time
import memory_match
import write_summary
import pyautogui as pag

def macro(times=12):
    time.sleep(3)
    collected = {}
    games = {'Regular':0, 'Mega':0, 'Night':0, 'Extreme':0, 'Winter':0}
    write_summary.clearFolder()

    try:
        for i in range(times):
            print('loop')
            type, cd = memory_match.initialize()

            if type:
                print('found')
                games[type] += 1

                if type != 'Extreme' and type != 'Winter':
                    items = memory_match.play(type)
                else:
                    items = memory_match.play(type, 16, (1919, 1019))

                collected = write_summary.identify(items, collected)
                print(collected)
            else:
                print('Not Found')

            if i != times - 1:
                for _ in range(cd):
                    print('begin')
                    time.sleep(15)#*60)
                    pag.press('\\', 2)
                    print('end')
    
    except KeyboardInterrupt:
        write_summary.writeSummary(collected, games)

macro()

# Add CD <-- This next?
# Add outside loop
# polish stuff
# ayaaa!!