path = "./mycaptcha.txt"
myfile = open(path, 'r')
captcha = myfile.read()
captcha = captcha[:-1] # remove newline character

curr = 0
next = 0
matched = []

for i,num in enumerate(captcha):
    curr = int(num)
    if i < len(captcha) - 1:
        next = int(captcha[i+1])
    else:
        next = int(captcha[0])
    if curr == next:
        print("match found: {} == {}".format(curr, next))
        matched.append(curr)

matched_sum = sum(matched)
print("sum of matched values:", matched_sum)