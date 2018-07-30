level_totals = {
    0: 1,
}

def get_highest_num(level):
    """ recursively build dictionary of highest numbers for each level """
    if level in level_totals:
        return level_totals[level]
    else:
        return get_highest_num(level - 1) + (level * 8)

def get_level(num):
    """ calculates which level a number is in """
    level = 0
    while True:
        if num <= get_highest_num(level):
            return level
        level += 1

def get_row_length(level):
    """ returns the length of one side of given level """
    if level == 0:
        return 1
    else:
        return level * 2 + 1

def is_corner_case(num, level):
    """ checks if the number is a corner case for a given level """
    corner_diff = get_row_length(level) - 1
    highest_num = get_highest_num(level)
    if num == highest_num:
        return True
    elif num == highest_num - corner_diff:
        return True
    elif num == highest_num - corner_diff * 2:
        return True
    elif num == highest_num - corner_diff * 3:
        return True
    return False
    
def print_info(num):
    """ prints infromation on the given number """
    level = get_level(num)
    row_length = get_row_length(level)
    corner_case = is_corner_case(num, level)
    print("for num {},\n\tthe level is {},\n\tthe row_length is {},\n\tthe corner_case is {}"
            .format(num, level, row_length, corner_case))

print_info(1)
print_info(12)
print_info(23)
print_info(1024)
