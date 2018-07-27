def build_table(file, table):
    for line in file:
        table.append(line.split())

def find_row_diff(row):
    max = int(row[0])
    min = int(row[0])
    for num in row:
        if int(num) > max:
            max = int(num)
        if int(num) < min:
            min = int(num)
    return max - min

path = "./myinput.txt"
myfile = open(path, 'r')

table = []
build_table(myfile, table)

diffs = []

for row in table:
    diffs.append(find_row_diff(row))

solution = sum(diffs)
print("checksum is:", solution)
