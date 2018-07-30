""" solutions for problems 1a and 1b """

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
