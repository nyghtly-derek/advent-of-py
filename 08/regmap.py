"""
--- Problem 8A ---

You receive a signal directly from the CPU. Because of your recent assistance with jump instructions, it would like you to compute the result of a series of unusual register instructions.

Each instruction consists of several parts: the register to modify, whether to increase or decrease that register's value, the amount by which to increase or decrease it, and a condition. If the condition fails, skip the instruction without modifying the register. The registers all start at 0. The instructions look like this:

b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10

These instructions would be processed as follows:

    Because a starts at 0, it is not greater than 1, and so b is not modified.
    a is increased by 1 (to 1) because b is less than 5 (it is 0).
    c is decreased by -10 (to 10) because a is now greater than or equal to 1 (it is 1).
    c is increased by -20 (to -10) because c is equal to 10.

After this process, the largest value in any register is 1.

You might also encounter <= (less than or equal to) or != (not equal to). However, the CPU doesn't have the bandwidth to tell you what all the registers are named, and leaves that to you to determine.

What is the largest value in any register after completing the instructions in your puzzle input?

--- Problem 8B ---

To be safe, the CPU also needs to know the highest value held in any register during this process so that it can decide how much memory to allocate to these operations. For example, in the above instructions, the highest value ever held was 10 (in register c after the third instruction was evaluated).

"""

def build_data(file):
    data = []
    for line in file:
        data.append(line.split())
    file.close()
    return data

def print_data(dataset):
    for elem in dataset:
        print("\t{}".format(elem))

def init_registry(instructions):
    regmap = {}
    for instruction in instructions:
        if instruction[0] not in regmap:
            regmap[instruction[0]] = 0
    return regmap

def print_registry(regmap):
    for key in regmap:
        print("\t{} -> {}".format(key,regmap[key]))

def update_registry(instructions, regmap):
    largest_ever = 0
    for instruction in instructions:
        new_reg = update_register(instruction, regmap)
        if new_reg > largest_ever:
            largest_ever = new_reg
    return largest_ever

def update_register(instruction, regmap):
    # makes you wish that you were coding in Rust amiright?
    reg_target = instruction[0]
    op = instruction[1]
    op_by = int(instruction[2])
    reg_cmp = instruction[4]
    comparison = instruction[5]
    cmp_to = int(instruction[6])
    condition_passed = False
    if comparison == '==':
        if regmap[reg_cmp] == cmp_to:
            condition_passed = True
    elif comparison == '!=':
        if regmap[reg_cmp] != cmp_to:
            condition_passed = True
    elif comparison == '>':
        if regmap[reg_cmp] > cmp_to:
            condition_passed = True
    elif comparison == '<':
        if regmap[reg_cmp] < cmp_to:
            condition_passed = True
    elif comparison == '>=':
        if regmap[reg_cmp] >= cmp_to:
            condition_passed = True
    elif comparison == '<=':
        if regmap[reg_cmp] <= cmp_to:
            condition_passed = True
    if condition_passed:
        if op == 'inc':
            regmap[reg_target] = regmap[reg_target] + op_by
        elif op == 'dec':
            regmap[reg_target] = regmap[reg_target] - op_by
    return regmap[reg_target]

def find_largest_value(regmap):
    return max(regmap.values())

path = "data/myinput.txt"
myfile = open(path, "r")
instructions = build_data(myfile)

print("dataset for file {} is:".format(path))
print_data(instructions)

regmap = init_registry(instructions)

print("regmap is:")
print_registry(regmap)

largest_ever = update_registry(instructions, regmap)
curr_largest = find_largest_value(regmap)

print("updated regmap is:")
print_registry(regmap)

print("\ncurrent largest value in regmap is: {}\n".format(curr_largest))
print("largest value ever in regmap is: {}\n".format(largest_ever))
