"""
--- Problem 11A ---

Crossing the bridge, you've barely reached the other side of the stream when a program comes up to you, clearly in distress. "It's my child process," she says, "he's gotten lost in an infinite grid!"

Fortunately for her, you have plenty of experience with infinite grids.

Unfortunately for you, it's a hex grid.

The hexagons ("hexes") in this grid are aligned such that adjacent hexes can be found to the north, northeast, southeast, south, southwest, and northwest:

  \ n  /
nw +--+ ne
  /    \
-+      +-
  \    /
sw +--+ se
  / s  \

You have the path the child process took. Starting where he started, you need to determine the fewest number of steps required to reach him. (A "step" means to move from the hex you are in to any adjacent hex.)

For example:

    ne,ne,ne is 3 steps away.
    ne,ne,sw,sw is 0 steps away (back where you started).
    ne,ne,s,s is 2 steps away (se,se).
    se,sw,se,sw,sw is 3 steps away (s,s,sw).

Your puzzle answer was 805.
--- Problem 11B ---

How many steps away is the furthest he ever got from his starting position?
"""

from const import COMBOS, CANCEL

def build_data(filepath):
    myfile = open(filepath, "r")
    data = []
    for line in myfile:
        data = line.split(',')
    myfile.close()
    return data

def find_shortest_path(opath):
    short_path = []
    furthest_traveled = 0
    for direction in opath:
        short_path = update_path(direction, short_path)
        if len(short_path) > furthest_traveled:
            furthest_traveled = len(short_path)
    return short_path, furthest_traveled

def update_path(latest_dir, path):
    path.append(latest_dir)
    condensing = True
    while condensing:
        condensing, path = condense_path(path)
    return path

def condense_path(path):
    if len(path) == 0:
        return (False, path)
    latest_dir = path[-1]
    for i, direction in enumerate(path[:-1]):
        if direction + latest_dir in CANCEL:
            newpath = path[:i] + path[i+1:-1]
            return (False, newpath) 
        elif direction + latest_dir in COMBOS:
            combo = COMBOS[direction + latest_dir]
            newpath = path[:i] + path[i+1:-1]
            newpath.append(combo) # combo will be available in next round of condensing
            return (True, newpath)
    return (False, path)
    
# declare file paths
my_input_path = 'data/myinput.txt'
test1_path = 'data/test1.txt'
test2_path = 'data/test2.txt'
test3_path = 'data/test3.txt'
test4_path = 'data/test4.txt'
test5_path = 'data/test5.txt'

# load in data
my_input_data = build_data(my_input_path)
test1_data = build_data(test1_path)
test2_data = build_data(test2_path)
test3_data = build_data(test3_path)
test4_data = build_data(test4_path)
test5_data = build_data(test5_path)

# test
assert find_shortest_path(test1_data)[0] == ['ne', 'ne', 'ne']
assert find_shortest_path(test2_data)[0] == []
assert find_shortest_path(test3_data)[0] == ['se', 'se']
assert find_shortest_path(test4_data)[0] == ['s', 's', 'sw']

# run
shortest_path, furthest_traveled = find_shortest_path(my_input_data)
#print(shortest_path)
print("length of shortest path", len(shortest_path))
print("furthest traveled", furthest_traveled)



