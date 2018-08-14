"""
--- Problem 9A ---

A large stream blocks your path. According to the locals, it's not safe to cross the stream at the moment because it's full of garbage. You look down at the stream; rather than water, you discover that it's a stream of characters.

You sit for a while and record part of the stream (your puzzle input). The characters represent groups - sequences that begin with { and end with }. Within a group, there are zero or more other things, separated by commas: either another group or garbage. Since groups can contain other groups, a } only closes the most-recently-opened unclosed group - that is, they are nestable. Your puzzle input represents a single, large group which itself contains many smaller ones.

Sometimes, instead of a group, you will find garbage. Garbage begins with < and ends with >. Between those angle brackets, almost any character can appear, including { and }. Within garbage, < has no special meaning.

In a futile attempt to clean up the garbage, some program has canceled some of the characters within it using !: inside garbage, any character that comes after ! should be ignored, including <, >, and even another !.

You don't see any characters that deviate from these rules. Outside garbage, you only find well-formed groups, and garbage always terminates according to the rules above.

Here are some self-contained pieces of garbage:

    <>, empty garbage.
    <random characters>, garbage containing random characters.
    <<<<>, because the extra < are ignored.
    <{!>}>, because the first > is canceled.
    <!!>, because the second ! is canceled, allowing the > to terminate the garbage.
    <!!!>>, because the second ! and the first > are canceled.
    <{o"i!a,<{i<a>, which ends at the first >.

Here are some examples of whole streams and the number of groups they contain:

    {}, 1 group.
    {{{}}}, 3 groups.
    {{},{}}, also 3 groups.
    {{{},{},{{}}}}, 6 groups.
    {<{},{},{{}}>}, 1 group (which itself contains garbage).
    {<a>,<a>,<a>,<a>}, 1 group.
    {{<a>},{<a>},{<a>},{<a>}}, 5 groups.
    {{<!>},{<!>},{<!>},{<a>}}, 2 groups (since all but the last > are canceled).

Your goal is to find the total score for all groups in your input. Each group is assigned a score which is one more than the score of the group that immediately contains it. (The outermost group gets a score of 1.)

    {}, score of 1.
    {{{}}}, score of 1 + 2 + 3 = 6.
    {{},{}}, score of 1 + 2 + 2 = 5.
    {{{},{},{{}}}}, score of 1 + 2 + 3 + 3 + 3 + 4 = 16.
    {<a>,<a>,<a>,<a>}, score of 1.
    {{<ab>},{<ab>},{<ab>},{<ab>}}, score of 1 + 2 + 2 + 2 + 2 = 9.
    {{<!!>},{<!!>},{<!!>},{<!!>}}, score of 1 + 2 + 2 + 2 + 2 = 9.
    {{<a!>},{<a!>},{<a!>},{<ab>}}, score of 1 + 2 = 3.

What is the total score for all groups in your input?

--- Problem 9B ---

Now, you're ready to remove the garbage.

To prove you've removed it, you need to count all of the characters within the garbage. The leading and trailing < and > don't count, nor do any canceled characters or the ! doing the canceling.

    <>, 0 characters.
    <random characters>, 17 characters.
    <<<<>, 3 characters.
    <{!>}>, 2 characters.
    <!!>, 0 characters.
    <!!!>>, 0 characters.
    <{o"i!a,<{i<a>, 10 characters.

How many non-canceled characters are within the garbage in your puzzle input?

"""

def build_data(file):
    data = ""
    for line in file:
        data = line
    file.close()
    return data

def print_data(dataset):
    print("\t{}".format(dataset))

def remove_canceled(stream):
    new_stream = ""
    i = 0
    while i < len(stream):
        char = stream[i]
        if char == '!':
            i += 1
        else:
            new_stream += char
        i += 1
    return new_stream
    
def remove_garbage(stream):
    total_rmvd = 0
    rm_from = 0
    opened = False
    rm_to = 0
    closed = False
    garbage_index = []
    for (i,char) in enumerate(stream):
        if char == '<':
            if not opened:
                rm_from = i
                opened = True
        if char == '>':
            if opened:
                rm_to = i
                closed = True
        if opened and closed:
            garbage_index.append((rm_from,rm_to))
            opened = False
            closed = False
            rm_from = 0
            rm_to = 0
    garbage_index.reverse()
    for rm_i in garbage_index:
        stream = stream[:rm_i[0]] + stream[rm_i[1]+1:]
        total_rmvd += (rm_i[1] - rm_i[0] - 1)
    return (stream, total_rmvd)

def calc_score(stream):
    total = 0
    level = 0
    for char in stream:
        if char == '{':
            level += 1
        elif char == '}':
            total += level
            level -=1
    return total

path = "data/myinput.txt"

print("for dataset {}:".format(path))

myfile = open(path, "r")
stream = build_data(myfile)

print("initial stream:")
print_data(stream)

stream = remove_canceled(stream)

print("after canceling:")
print_data(stream)

stream_after_garbage = remove_garbage(stream)
stream = stream_after_garbage[0]
total_removed = stream_after_garbage[1]

print("after tossing garbage:")
print_data(stream)

score = calc_score(stream)

print("group score is {}\n".format(score))
print("amount garbage removed is {}\n".format(total_removed))