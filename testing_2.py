collected = {}
games = {'Regular':0, 'Mega':0, 'Night':0, 'Extreme':0, 'Winter':0}

def macro(collected):

    type = 'Regular'
    if type:
        games[type] += 1

        collected = collected
    print(collected, games)

macro(collected)