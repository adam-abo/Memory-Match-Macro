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
            type, cd = memory_match.initialize()

            if type:
                games[type] += 1

                try:
                    if type != 'Extreme' and type != 'Winter':
                        items = memory_match.play(type)
                    else:
                        items = memory_match.play(type, 16, (1919, 1019), (930, 535))
                    collected = write_summary.identify(items, collected)
                    print(collected)

                except SystemExit:
                    print('holding game open for ma lord')
                    for _ in range(100):
                        time.sleep(15*60)
                        pag.press('k')

            else:
                print('Not Found')

            if i != times - 1:
                for _ in range(cd):
                    time.sleep(15*60)
                    pag.press('k')
        write_summary.writeSummary(collected, games)

    except KeyboardInterrupt:
        write_summary.writeSummary(collected, games)

macro(1)

# Add CD <-- This next?
# UI nav breaking bug
# Add outside loop
# polish stuff
# ayaaa!!