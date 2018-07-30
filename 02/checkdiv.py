def build_table(file, table):
    for line in file:
        table.append(line.split())

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
