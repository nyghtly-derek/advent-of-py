"""
--- Problem 3B ---

As a stress test on the system, the programs here clear the grid and then store the value 1 in square 1. Then, in the same allocation order as shown above, they store the sum of the values in all adjacent squares, including diagonals.

So, the first few squares' values are chosen as follows:

    Square 1 starts with the value 1.
    Square 2 has only one adjacent filled square (with value 1), so it also stores 1.
    Square 3 has both of the above squares as neighbors and stores the sum of their values, 2.
    Square 4 has all three of the aforementioned squares as neighbors and stores the sum of their values, 4.
    Square 5 only has the first and fourth squares as neighbors, so it gets the value 5.

Once a square is written, its value does not change. Therefore, the first few squares would receive the following values:

147  142  133  122   59
304    5    4    2   57
330   10    1    1   54
351   11   23   25   26
362  747  806--->   ...

What is the first value written that is larger than your puzzle input?
"""

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