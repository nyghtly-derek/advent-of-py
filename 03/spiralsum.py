""" solution for problem 3b """

def build_spiral_map(target):
    smap = {(0,0):1}
    pos = (1,0)
    lvl = 1
    next_lvl = 2
    solved = False
    while not solved:
        while lvl < next_lvl:
            smap[pos] = calc_next_value(pos, smap)
            if smap[pos] >= target:
                solved = True
                break
            pos = update_pos(pos, lvl)
            if pos[0] > lvl:
                lvl += 1
                next_lvl += 1
    return smap

def calc_next_value(pos, smap):
    total = 0
    positions = []
    for x in range(-1,2):
        for y in range(-1,2):
            if not (x == 0 and y == 0):
                new = (pos[0] + x, pos[1] + y)
                positions.append(new)
    for newpos in positions:
        if newpos in smap:
            total += smap[newpos]
    return total

def update_pos(pos, level):
    if pos == (level, -level):
        # pos is southeast corner of current level
        return (pos[0] + 1, pos[1])
    elif pos[0] == level and pos[1] != level:
        # pos is east but not northeast corner 
        return (pos[0], pos[1] + 1)
    elif pos[0] != -level and pos[1] == level:
        # north except northwest corner
        return (pos[0] - 1, pos[1])
    elif pos[0] == -level and pos[1] != -level:
        # west except southwest corner
        return (pos[0], pos[1] - 1)
    else:
        # south except southeast corner
        return (pos[0] + 1, pos[1])

target = 325489
spiralmap = build_spiral_map(target+1)
for key in spiralmap:
    print("{}  \t->\t{}".format(key, spiralmap[key]))