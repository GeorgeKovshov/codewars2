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


def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

def even_or_odd2(number):
	return 'Odd' if number % 2 else 'Even'


def sum_two_smallest_numbers(numbers):
    min1 = min(numbers)
    numbers.remove(min1)
    min2 = min(numbers)
    return min1 + min2

def sum_two_smallest_numbers2(numbers):
    return sum(sorted(numbers)[:2])

print(sum_two_smallest_numbers([5, 8, 12, 2, 18, 22]))

import math
def nb_year(p0, percent, aug, p):
    years = 0
    while p0 < p:
        p0 += math.floor(p0 * (percent * 0.01)) + aug
        print(str(p0) + " on year " + str(years))
        years += 1
    return years

def nb_year2(p0, percent, aug, p, years = 0):
    if p0 < p:
        return nb_year(p0 + int(p0 * percent / 100) + aug, percent, aug, p, years + 1)
    return years

print(nb_year(1000, 2, 50, 1214))

def find_needle(haystack):
    result = "found the needle at position " + str(haystack.index("needle"))
    return result

def find_needle2(haystack): return 'found the needle at position %d' % haystack.index('needle')

print(find_needle(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]))












