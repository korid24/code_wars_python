array = [[1,2,3],
         [4,5,6],
         [7,8,9]]

def snail(snail_map):
    direction = 'right'
    snail= []
    map = snail_map
    while map != []:
        if direction == 'right':
            snail += map.pop(0)
            direction = 'down'
        elif direction == 'down':
            for i in range(len(map)):
                snail.append(map[i].pop(-1))
            direction = 'left'
        elif direction == 'left':
            snail += reversed(map.pop(-1))
            direction = 'top'
        else:
            for i in range(len(map))[::-1]:
                snail.append(map[i].pop(0))
            direction = 'right'
    return snail

print(snail(array))
