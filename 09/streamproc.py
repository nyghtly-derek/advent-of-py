def build_data(file):
    data = file
    file.close()
    return data

def print_data(dataset):
    for elem in dataset:
        print("\t{}".format(elem))
    
path = "data/easy.txt"
myfile = open(path, "r")
data = build_data(myfile)

print("for dataset {}:".format(path))
print_data(data)
