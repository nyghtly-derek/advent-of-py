"""
--- Problem 5B ---

Now, the jumps are even stranger: after each jump, if the offset was three or more, instead decrease it by 1. Otherwise, increase it by 1 as before.

Using this rule with the above example, the process now takes 10 steps, and the offset values after finding the exit are left as 2 3 2 3 -1.

How many steps does it now take to reach the exit?
"""

def build_data(file):
    data = []
    for line in file:
        jumpnum = int(line)
        data.append(jumpnum)
    return data

def print_data(datalist):
    for elem in datalist:
        print("\t{}".format(elem))

def maze_jumper(jumplist):
    curr_index = 0
    curr_num = jumplist[0]
    stuck_in_maze = True
    steps = 0
    while stuck_in_maze:
        steps += 1
        if curr_num >= 3:
            jumplist[curr_index] -= 1
        else:
            jumplist[curr_index] += 1
        next_index = curr_index + curr_num
        if next_index >= len(jumplist):
            break # out of bounds
        elif next_index < 0:
            break # out of bounds
        else:
            curr_index = next_index
        curr_num = jumplist[curr_index]
    return steps

path = "data/myinput.txt"
myfile = open(path, "r")

jumpnums = build_data(myfile)

print("for dataset {}:".format(path))
print_data(jumpnums)
print("num jumps is", maze_jumper(jumpnums))
