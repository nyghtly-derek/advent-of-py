def build_data(file):
    data = []
    for line in file:
        data = line.split()
    return data

def print_data(dataset):
    print("\t{}".format(dataset))

def data_to_int(dataset):
    for i, elem in enumerate(dataset):
        dataset[i] = int(elem)

def balance_mem(memory):
    ihigh = get_index_highest(memory)
    blocks_to_give = memory[ihigh]
    memory[ihigh] = 0
    give_blocks(memory, blocks_to_give, ihigh)
    print("\t{}".format(memory))

def get_index_highest(memory):
    highest = 0
    index_highest = 0
    for i,membank in enumerate(memory):
        if membank > highest:
            index_highest = i
            highest = membank
    return index_highest

def give_blocks(memory, numblocks, index_from):
    i = index_from + 1
    while numblocks > 0:
        while i < len(memory):
            if numblocks > 0:
                memory[i] += 1
                numblocks -= 1
            i += 1
        i = 0

def find_repeat_cycle(memory):
    num_cycles = 0
    past_memory = [[memory.copy()]]
    while True:
        balance_mem(memory)
        num_cycles += 1
        if memory in past_memory:
            return num_cycles
        else:
            past_memory.append(memory.copy())

path = "data/myinput.txt"
myfile = open(path, "r")
membanks = build_data(myfile)
data_to_int(membanks)

print("for dataset {}:".format(path))
print_data(membanks)
print("reallocating memory...")
print("num cycles until repeated memory:", find_repeat_cycle(membanks))