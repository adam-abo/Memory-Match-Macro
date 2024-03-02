import time
import memory_match

time.sleep(3)
type = memory_match.initialize()

if type:
    if type > 2:
        print(memory_match.play(type))
    else:
        print(memory_match.play(type, 16, (1919, 1019)))
else:
    print('Not Found')

# Add CD <-- This next?
# Add outside loop
# Item Summary <-- This next?
# polish stuff
#Hey bud