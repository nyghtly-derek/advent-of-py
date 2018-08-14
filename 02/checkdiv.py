""" 
--- Problem 2B ---

"Great work; looks like we're on the right track after all. Here's a star for your effort." However, the program seems a little worried. Can programs be worried?

"Based on what we're seeing, it looks like all the User wanted is some information about the evenly divisible values in the spreadsheet. Unfortunately, none of us are equipped for that kind of calculation - most of us specialize in bitwise operations."

It sounds like the goal is to find the only two numbers in each row where one evenly divides the other - that is, where the result of the division operation is a whole number. They would like you to find those numbers on each line, divide them, and add up each line's result.

For example, given the following spreadsheet:

5 9 2 8
9 4 7 3
3 8 6 5

    In the first row, the only two numbers that evenly divide are 8 and 2; the result of this division is 4.
    In the second row, the two numbers are 9 and 3; the result is 3.
    In the third row, the result is 2.

In this example, the sum of the results would be 4 + 3 + 2 = 9.

What is the sum of each row's result in your puzzle input?
"""

def build_table(file, table):
    for line in file:
        table.append(line.split())
    file.close()

def find_row_div(row):
    for i,num1 in enumerate(row):
        for j,num2 in enumerate(row):
            if i != j:
                rtn = compare_divs(int(num1), int(num2))
                if rtn >= 0:
                    return rtn
    return -1

def compare_divs(num1, num2) -> int:
    if num1 % num2 == 0:
        if num1 > num2:
            return int(num1 / num2)
        else:
            return int(num2 / num1)
    return -1

path = "data/myinput.txt"
myfile = open(path, 'r')

table = []
build_table(myfile, table)

divs = []

for row in table:
    divs.append(find_row_div(row))

solution = sum(divs)
print("checkdiv is:", solution)
