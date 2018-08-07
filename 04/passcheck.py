"""
--- Problem 4A ---

A new system policy has been put in place that requires all accounts to use a passphrase instead of simply a password. A passphrase consists of a series of words (lowercase letters) separated by spaces.

To ensure security, a valid passphrase must contain no duplicate words.

For example:

    aa bb cc dd ee is valid.
    aa bb cc dd aa is not valid - the word aa appears more than once.
    aa bb cc dd aaa is valid - aa and aaa count as different words.

The system's full passphrase list is available as your puzzle input. How many passphrases are valid?
"""

def build_data(file):
    data = []
    for line in file:
        data.append(line.split())
    return data

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

passphrases = build_data(myfile)

print("for dataset:")
print_data(passphrases)
print("num valid is:", count_valid(passphrases))