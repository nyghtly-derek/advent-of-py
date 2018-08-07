""" 
Problem 1:

--- Part A: ---

You're standing in a room with "digitization quarantine" written in LEDs along 
one wall. The only door is locked, but it includes a small interface. "Restricted 
Area - Strictly No Digitized Users Allowed."

It goes on to explain that you may only leave by solving a captcha to prove you're 
not a human. Apparently, you only get one millisecond to solve the captcha: too fast 
for a normal human, but it feels like hours to you.

The captcha requires you to review a sequence of digits (your puzzle input) and find 
the sum of all digits that match the next digit in the list. The list is circular, 
so the digit after the last digit is the first digit in the list.

For example:

    1122 produces a sum of 3 (1 + 2) because the first digit (1) matches the second digit and the third digit (2) matches the fourth digit.
    1111 produces 4 because each digit (all 1) matches the next.
    1234 produces 0 because no digit matches the next.
    91212129 produces 9 because the only digit that matches the next one is the last digit, 9.

What is the solution to your captcha?

--- Part B: ---

You notice a progress bar that jumps to 50% completion. Apparently, the door isn't yet 
satisfied, but it did emit a star as encouragement. The instructions change:

Now, instead of considering the next digit, it wants you to consider the digit halfway 
around the circular list. That is, if your list contains 10 items, only include a digit 
in your sum if the digit 10/2 = 5 steps forward matches it. Fortunately, your list has 
an even number of elements.

For example:

    1212 produces 6: the list contains 4 items, and all four digits match the digit 2 items ahead.
    1221 produces 0, because every comparison is between a 1 and a 2.
    123425 produces 4, because both 2s match each other, but no other digit has a match.
    123123 produces 12.
    12131415 produces 4.

What is the solution to your new captcha?

"""

def solve_captcha_a(data):
    curr = 0
    next = 0
    matched = []

    for i,num in enumerate(data):
        curr = int(num)
        if i < len(data) - 1:
            next = int(data[i+1])
        else:
            next = int(data[0])
        if curr == next:
            #print("match found: {} == {}".format(curr, next))
            matched.append(curr)

    return sum(matched)

def solve_captcha_b(data):
    curr = 0
    next = 0
    matched = []
    full_len = len(data)
    half_len = int(len(data)/2)

    for i,num in enumerate(data):
        curr = int(num)
        if i < len(data) - half_len:
            next_index = i + half_len
            next = int(data[next_index])
        else:
            remaining = half_len - (full_len - i)
            next = int(data[remaining])
        if curr == next:
            #print("match found: {} == {}".format(curr, next))
            matched.append(curr)

    return sum(matched)

def main():
    path = "input/mycaptcha.txt"
    myfile = open(path, 'r')
    captcha = myfile.read()

    if captcha[-1] == '\n':
        captcha = captcha[:-1] 
    
    print("dataset:\n")
    print(captcha)
    solution_a = solve_captcha_a(captcha)
    solution_b = solve_captcha_b(captcha)
    print("\nsolution to problem a:", solution_a)
    print("solution to problem b:", solution_b)


if __name__ == "__main__":
    main()
