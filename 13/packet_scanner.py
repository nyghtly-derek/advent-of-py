def read_firewall_data(path):
	data = []
	with open(path, 'r') as myfile:
		for line in myfile:
			data.append(line.rstrip())
	return data

def build_firewall_map(firewall_raw_data):
	firewall_map = {}
	for data_pair in firewall_raw_data:
		split_pair = data_pair.split(': ')
		layer_depth = int(split_pair[0])
		layer_range = int(split_pair[1])
		firewall_map[layer_depth] = layer_range
	return firewall_map

def get_max_depth(firewall_raw_data):
	return int(firewall_raw_data[-1].split(': ')[0])

def scanner_at_position_zero(picosecond, layer_depth, firewall_map):
	if layer_depth in firewall_map:
		layer_range = firewall_map[layer_depth]
		if ( picosecond % ( 2 * ( layer_range - 1 ) ) ) == 0:
			return True
	return False

def packet_detected(picosecond, depth, firewall_map):
	if scanner_at_position_zero(picosecond, depth, firewall_map):
		return True
	else:
		return False

def get_severity(layer_depth, firewall_map):
	return firewall_map[layer_depth] * layer_depth

def traverse_firewall(picosecond, firewall_map, max_depth):
	severity = 0
	depth_traveled = 0
	caught = False
	while depth_traveled <= max_depth:
		if packet_detected(picosecond, depth_traveled, firewall_map):
			#print(f'packet detected! \n-> picosecond:\t {picosecond}')
			severity += get_severity(depth_traveled, firewall_map)
			caught = True
		picosecond += 1
		depth_traveled += 1
	return (severity, caught)

def find_vulnurability(picosecond, firewall_map, max_depth):
	depth_traveled = 0
	while depth_traveled <= max_depth:
		if packet_detected(picosecond, depth_traveled, firewall_map):
			#print(f'packet detected! \n-> picosecond:\t {picosecond}')
			return False
		picosecond += 1
		depth_traveled += 1
	return True

path = 'data/my_input.txt'
data = read_firewall_data(path)
firewall_map = build_firewall_map(data)
max_depth = get_max_depth(data)

print(f'for dataset {path}:\n')

severity, caught = traverse_firewall(0, firewall_map, max_depth)

print(f'total severity at first attempt: {severity}')

picosecond = 0
vulnurability_found = False
try:
	while not vulnurability_found:
		picosecond += 1
		if picosecond % 1000000 == 0:
			print(f'checking for vulnurability at picosecond {picosecond}')
		vulnurability_found = find_vulnurability(picosecond, firewall_map, max_depth)
	print('vulnurability found!')
	print(f'wait {picosecond} picoseconds')
except:
	print(f'failed to bypass firewall')
	