""" solution for problem 3b """

def build_spiral_map(target):
    smap = {(0,0):1}
    pos = [1,0]
    lvl = 1
    next_lvl = 2
    solved = False
    while not solved:
        while lvl < next_lvl:
            pos_as_tuple = tuple(pos)
            smap[pos_as_tuple] = calc_next_value(pos, smap)
            if smap[pos_as_tuple] >= target:
                solved = True
                break
            pos = update_pos(pos, lvl)
            if pos[0] > lvl:
                lvl += 1
                next_lvl += 1
    return smap

def calc_next_value(pos, smap):
    north = [pos[0], pos[1] + 1]
    south = [pos[0], pos[1] - 1]
    east = [pos[0] + 1, pos[1]]
    west = [pos[0] - 1, pos[1]]
    north_east = [pos[0] + 1, pos[1] + 1]
    north_west = [pos[0] - 1, pos[1] + 1]
    south_east = [pos[0] + 1, pos[1] - 1] 
    south_west = [pos[0] - 1, pos[1] - 1] 
    positions = [north, south, east, west, north_east, 
                 north_west, south_east, south_west]
    for i in range(len(positions)):
        positions[i] = tuple(positions[i])
    total = 0
    for newpos in positions:
        if newpos in smap:
            total += smap[newpos]
    return total

def update_pos(pos, level):
    if pos == [level, -level]:
        # pos is southeast corner of current level
        return [pos[0] + 1, pos[1]]
    elif pos[0] == level and abs(pos[1]) != level:
        # pos is east but not a corner case
        return [pos[0], pos[1] + 1]
    elif pos == [level, level]:
        # northeast corner
        return [pos[0] - 1, pos[1]]
    elif pos[1] == level and abs(pos[0]) != level:
        # north not corner
        return [pos[0] - 1, pos[1]]
    elif pos == [-level, level]:
        # northwest corner
        return [pos[0], pos[1] - 1]
    elif pos[0] == -level and abs(pos[1]) != level:
        # west not corner
        return [pos[0], pos[1] - 1]
    elif pos == [-level, -level]:
        # southwest corner
        return [pos[0] + 1, pos[1]]
    elif pos[1] == -level and abs(pos[0]) != level:
        # south not corner
        return [pos[0] + 1, pos[1]]

    
spiralmap = build_spiral_map(325490)
for key in spiralmap:
    print("{}  \t->\t{}".format(key, spiralmap[key]))