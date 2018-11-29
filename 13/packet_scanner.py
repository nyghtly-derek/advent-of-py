import pprint as ppr

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

def scanner_at_position_zero(layer_depth, picosecond, firewall_map):
	if layer_depth in firewall_map:
		layer_range = firewall_map[layer_depth]
		if ( picosecond % ( 2 * ( layer_range - 1 ) ) ) == 0:
			return True
	return False

def packet_detected(picosecond, firewall_map):
	if scanner_at_position_zero(picosecond, picosecond, firewall_map):
		return True
	else:
		return False

def get_severity(layer_depth, firewall_map):
	return firewall_map[layer_depth] * layer_depth

path = 'data/my_input.txt'
data = read_firewall_data(path)
firewall_map = build_firewall_map(data)
max_depth = get_max_depth(data)
picosecond = 0
severity = 0

print(f'for dataset {path}:\n')

while picosecond <= max_depth:
	if packet_detected(picosecond, firewall_map):
		print(f'packet detected! \n-> picosecond:\t {picosecond}')
		severity += get_severity(picosecond, firewall_map)
	picosecond += 1

print(f'\ntotal severity: {severity}')