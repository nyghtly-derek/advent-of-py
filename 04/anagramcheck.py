"""
Problem 4, Part B:

For added security, yet another system policy has been put in place. Now, a valid passphrase must contain no two words that are anagrams of each other - that is, a passphrase is invalid if any word's letters can be rearranged to form any other word in the passphrase.

For example:

    abcde fghij is a valid passphrase.
    abcde xyz ecdab is not valid - the letters from the third word can be rearranged to form the first word.
    a ab abc abd abf abj is a valid passphrase, because all letters need to be used when forming another word.
    iiii oiii ooii oooi oooo is valid.
    oiii ioii iioi iiio is not valid - any of these words can be rearranged to form any other word.

Under this new system policy, how many passphrases are valid?
"""

def build_data(file):
    data = []
    for line in file:
        data.append(line.split())
    file.close()
    return data

def is_valid(passphrase):
    used_words = set()
    for word in passphrase:
        sorted_word = ''.join(sorted(word))
        if sorted_word in used_words:
            return False
        else:
            used_words.add(sorted_word)
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

print("for dataset {}:".format(path))
print_data(passphrases)
print("num valid is:", count_valid(passphrases))