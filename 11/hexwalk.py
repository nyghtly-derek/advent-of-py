import pprint as pp
from const import COMBOS, CANCEL

def build_data(filepath):
    myfile = open(path, "r")
    data = []
    for line in myfile:
        data = line.split(',')
    myfile.close()
    return data

def find_shortest_path(opath):
    short_path = []
    for direction in opath:
        short_path = update_path(direction, short_path)
    return short_path

def update_path(latest_dir, path):
    path.append(latest_dir)
    condensing = True
    while condensing:
        result = condense_path(path)
        condensing = result[0]
        path = result[1]
    return path

def condense_path(path):
    latest_dir = path[-1]
    #for direction in reversed(path[:-1]):
    #    if  
    return (False, path)
    
path = "data/test1.txt"
data = build_data(path)
pp.pprint(data)
shortest_path = find_shortest_path(data)
pp.pprint(shortest_path)


