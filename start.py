def last_survivor(letters, coords):
    #letter_list = [*letters]
    letter_list = [letter for letter in letters]
    for num in coords:
        letter_list.pop(num)
    i = 0
    result = ""
    while i < len(letter_list):
        result += str(letter_list[i])
        i+=1
    return result

def last_survivor2(letters, coords):
    l=[x for x in letters]
    [l.pop(x) for x in coords]
    return l[0]

print(last_survivor('abc', [1, 1]))


def solution(s):
    first_list = [*s]
    result = []
    i = 0
    while i < len(first_list) - 1:
        result.append(str(first_list[i]) + str(first_list[i+1]))
        i = i + 2
    if len(first_list) % 2 == 1:
        result.append(str(first_list[-1]) + "_")
    return result

#import re

#def solution(s):
#    return re.findall(".{2}", s + "_")

print(solution("inphf"))


