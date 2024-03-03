import time
import memory_match
import testing

collected = {}
time.sleep(3)
type = memory_match.initialize()

if type:
    if type > 2:
        items = memory_match.play(type)
    else:
        items = memory_match.play(type, 16, (1919, 1019))

    collected = testing.identify(items, collected)
else:
    print('Not Found')
    
print(collected)

# Add CD <-- This next?
# Add outside loop
# Item Summary <-- This next?
# polish stuff
#Hey bud