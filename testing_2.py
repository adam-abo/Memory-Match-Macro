def itemsMatched(items):
    items.sort()
    matched = []
    for item in items:
        if item[4]:
            matched.append(item[:4])
    matched.sort()
    matched = matched[::2]
    
    for item in matched:
        if matched.count(item) == 2:
            matched.remove(item)
            matched[matched.index(item)] = item[:3] + (item[3]*2,)
            break
    return matched

tiles = [(216, 72, 65, 25, 1), (136, 99, 163, 3, 1), (136, 99, 163, 3, 1), (183, 183, 183, 2, 1), (136, 99, 163, 3, 1), (216, 72, 65, 25, 1), (183, 183, 183, 2, 1), (136, 99, 163, 3, 1)]
print(tiles)
print(itemsMatched(tiles))