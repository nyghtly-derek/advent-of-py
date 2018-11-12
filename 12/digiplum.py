"""
--- Problem 12A: Digital Plumber ---

--- Part A ---

Walking along the memory banks of the stream, you find a small village that is experiencing a little confusion: some programs can't communicate with each other.

Programs in this village communicate using a fixed system of pipes. Messages are passed between programs using these pipes, but most programs aren't connected to each other directly. Instead, programs pass messages between each other until the message reaches the intended recipient.

For some reason, though, some of these messages aren't ever reaching their intended recipient, and the programs suspect that some pipes are missing. They would like you to investigate.

You walk through the village and record the ID of each program and the IDs with which it can communicate directly (your puzzle input). Each program has one or more programs with which it can communicate, and these pipes are bidirectional; if 8 says it can communicate with 11, then 11 will say it can communicate with 8.

You need to figure out how many programs are in the group that contains program ID 0.

For example, suppose you go door-to-door like a travelling salesman and record the following list:

0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5

In this example, the following programs are in the group that contains program ID 0:

    Program 0 by definition.
    Program 2, directly connected to program 0.
    Program 3 via program 2.
    Program 4 via program 2.
    Program 5 via programs 6, then 4, then 2.
    Program 6 via programs 4, then 2.

Therefore, a total of 6 programs are in this group; all but program 1, which has a pipe that connects it to itself.

How many programs are in the group that contains program ID 0?

--- Part Two ---

There are more programs than just the ones in the group containing program ID 0. The rest of them have no way of reaching that group, and still might have no way of reaching each other.

A group is a collection of programs that can all communicate via pipes either directly or indirectly. The programs you identified just a moment ago are all part of the same group. Now, they would like you to determine the total number of groups.

In the example above, there were 2 groups: one consisting of programs 0,2,3,4,5,6, and the other consisting solely of program 1.

How many groups are there in total?

"""

import pprint as ppr

def read_plumbing_data(path):
	connected_sets = []
	with open(path, 'r') as myfile:
		for line in myfile:
			connected_sets = add_connections(line, connected_sets)
			merge_again = True
			while merge_again:
				connected_sets, merge_again = merge_sets(connected_sets)
	return connected_sets
    
def add_connections(line, existing_sets):
	new_connections = parse_line(line)
	for i, cset in enumerate(existing_sets):
		if new_connections & cset:
			existing_sets[i] = cset | new_connections
			return existing_sets
	existing_sets.append(new_connections)
	return existing_sets

def parse_line(line):
	line = line.rstrip()
	line = line.split(' <-> ')
	connected = [line[0]] + line[1].split(', ')
	cset = set(connected)
	return cset

def merge_sets(existing_sets):
	for index_a, a in enumerate(existing_sets):
		for index_b, b in enumerate(existing_sets):
			if index_a != index_b:
				if a & b:
					existing_sets.append(a | b)
					existing_sets.remove(a)
					existing_sets.remove(b)
					return (existing_sets, True)
	return (existing_sets, False)

def num_connected_to_program_zero(connected_sets):
	for cset in connected_sets:
		if '0' in cset:
			return len(cset)
	return -1

path = 'data/myinput.txt'
connections = read_plumbing_data(path)
num_with_zero = num_connected_to_program_zero(connections)

print(f'-- for dataset {path} --')
#print('connected sets are:')
#ppr.pprint(connections)
print(f'number of programs in zero group: \n-> {num_with_zero}')
print(f'total number of separate groups: \n-> {len(connections)}')
