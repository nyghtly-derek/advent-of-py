def build_data(filepath):
    myfile = open(path, "r")
    data = []
    for line in myfile:
        data = line.split()
    myfile.close()
    return data

def print_data(dataset):
    for elem in dataset:
        print("\t{}".format(elem))
    
path = "data/easy.txt"
data = build_data(filepath)

print("for dataset {}:".format(path))
print_data(data)
