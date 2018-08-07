def build_data(file, table):
    for line in file:
        passphrases.append(line.split())

def is_valid(passphrase):
    used_words = set()
    for word in passphrase:
        if word in used_words:
            return False
        else:
            used_words.add(word)
    return True

def count_valid(dataset):
    count = 0
    for phrase in dataset:
        if is_valid(phrase):
            count += 1
    return count

def print_data(dataset):
    for phrase in dataset:
        print("\t{}".format(phrase))

path = "data/myinput.txt"
myfile = open(path, "r")

passphrases = []
build_data(myfile, passphrases)

print("for dataset:")
print_data(passphrases)
print("num valid is:", count_valid(passphrases))