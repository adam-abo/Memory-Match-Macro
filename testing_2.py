current_collected = {'Watermelon':1}
collected = {}

for item in current_collected:
            if item[:3] in collected:
                collected[item[:3]] += item[3]
            else:
                collected[item[:3]] = item[3]
print(collected)
for item in current_collected:
            if item[:3] in collected:
                collected[item[:3]] += item[3]
            else:
                collected[item[:3]] = item[3]
print(collected)