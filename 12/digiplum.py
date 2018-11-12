import pprint as ppr

def build_data(path):
	data = []
	with open(path, 'r') as myfile:
		for line in myfile:
			data.append(line.rstrip())
	return data
    
path = "data/easy.txt"
data = build_data(path)

print(f"for dataset {path}:")
ppr.pprint(data)
