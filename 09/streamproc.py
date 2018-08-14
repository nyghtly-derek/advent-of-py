def build_data(file):
    data = ""
    for line in file:
        data = line
    file.close()
    return data

def print_data(dataset):
    print("\t{}".format(dataset))

def remove_canceled(stream):
    new_stream = ""
    i = 0
    while i < len(stream):
        char = stream[i]
        if char == '!':
            i += 1
        else:
            new_stream += char
        i += 1
    return new_stream
    
def remove_garbage(stream):
    rm_from = 0
    opened = False
    rm_to = 0
    closed = False
    garbage_index = []
    for (i,char) in enumerate(stream):
        if char == '<':
            if not opened:
                rm_from = i
                opened = True
        if char == '>':
            if opened:
                rm_to = i
                closed = True
        if opened and closed:
            garbage_index.append((rm_from,rm_to))
            opened = False
            closed = False
            rm_from = 0
            rm_to = 0
    garbage_index.reverse()
    for rm_i in garbage_index:
        stream = stream[:rm_i[0]] + stream[rm_i[1]+1:]
    return stream

path = "data/myinput.txt"

print("for dataset {}:".format(path))

myfile = open(path, "r")
stream = build_data(myfile)

print("initial stream:")
print_data(stream)

stream = remove_canceled(stream)

print("after canceling:")
print_data(stream)

stream = remove_garbage(stream)

print("after tossing garbage:")

print_data(stream)