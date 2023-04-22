import math


def solution(s, t):
    base = s * t
    summ = base + s
    if summ > base:
        base = summ
    j = 1
    t -= 3
    while t >= 0:
        var = 3*(s - j)
        summ += -2*s + var
        t -= 2
        j += 1
        if summ < base:
            break
        else:
            base = summ
    return base


def solution2(s, t):
    # Sprints are optimally placed at the end of the race
    '''
    It is always beneficial to sprint at the end of the race
    Sprints are optimally placed at the end of the race
    e.g. RRRR...(SR)[n]S
    We take a run without sprints are keep adding sprints at
    the latest possible point until adding a sprint stops
    increasing the total distance travelled

    We can treat the final sprint as an add-on and count the number of
    (SR) units we introduce into the race. Looking at this, each add
    on unit changes the distance from 2*s to (3*s-3*n), so altering
    the distance by (s-3*n). We find the largest n<s for which (s-3*n)>0
    to find the trade-off point. If this is longer than the race in general
    we do as many (SR) as possible.
    '''
    trade_off = s // 3
    best_n_rs = min((t - 1) // 2, trade_off)  # trade off must be less than max available slots
    d = lambda n: s * t + s * (n + 1) - 3 / 2 * n * (n + 1)
    return d(best_n_rs)

def solution3(s, t):
    n = min((t-1)//2, s//3)
    return t*s + (n+1)*s - 3*(n+1)*n//2 if t else 0


print(solution(2,4))



def check_sides(str, width):
    perimeter = 0
    if str[0] == "X":
         perimeter += 1
    if str[width - 1] == "X":
        perimeter += 1
    return perimeter


def land_perimeter(arr):
    width = len(arr[0])
    length = len(arr)
    previous = "O" * width
    perimeter = 0
    i = 0
    while i < length:
        for j in range(width):
            if previous[j] != arr[i][j]:
                perimeter += 1
            if j < width-1:
                if arr[i][j] != arr[i][j+1]:
                    perimeter += 1

        perimeter += check_sides(arr[i], width)
        previous = arr[i]
        i += 1
    perimeter += arr[length-1].count("X")
    return perimeter


land = ['XOOXO',
        'XOOXO',
        'OOOXO',
        'XXOXO',
        'OXOOO']

print(land_perimeter(land))

import math

# TODO: complete this class

class PaginationHelper:

    # The constructor takes in an array of items and an integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        print(collection, items_per_page)
        self.collection = collection
        self.items_per_page = items_per_page
        self.items_amount = len(collection)
        self.page_amount = math.ceil(self.items_amount / self.items_per_page)
        c = 0
        tmp2 = []
        for i in range(self.page_amount):
            tmp = []
            for j in range(items_per_page):
                tmp.append(collection[c])
                c += 1
                if c > self.items_amount-1:
                    break
            tmp2.append(tmp)
        self.collection_pages = tmp2

    # returns the number of items within the entire collection
    def item_count(self):
        return self.items_amount

    # returns the number of pages
    def page_count(self):
        return self.page_amount


    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if page_index < 0 or page_index > self.page_amount-1:
            return -1
        else:
            return len(self.collection_pages[page_index])

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if item_index < 0 or item_index > self.items_amount-1:
            return -1
        elif item_index == 0:
            return 0
        else:
            page_index = -1
            things = 0
            while things < item_index:
                things += self.items_per_page
                page_index += 1
            return page_index



helper = PaginationHelper(['a','b','c','d','e','f'], 4)
print(helper.collection_pages)

print(helper.page_index(5))
print(land[-1])

def permutate():
    result = []
    for x in range(1,6):
        for y in range(1,6):
            for z in range(1,6):
                for w in range(1,6):
                    for d in range(1, 6):
                        tmp = set([x,y,z,w,d])
                        if len(tmp) == 5:
                            if x==1 or y==2 or z==3 or w==4 or d==5:
                                result.append([x,y,z,w,d])
    print(len(result))


def solve(input_string):
    list = input_string.split("\n")
    carry_list = ""
    for pair in list:
        carry_digit = 0
        carry_amount = 0
        length = len(pair) // 2
        i = length-1
        while i>=0:
            sum = int(pair[i])+ int(pair[length+1 + i]) + carry_digit
            print(int(pair[i]),'+', int(pair[length+1 + i]), '=', sum)
            carry_digit = sum // 10
            if carry_digit>0:
                carry_amount += 1
            i -= 1
        if carry_amount == 0:
            carry_list += "No carry operation\n"
        else:
            carry_list += f"{carry_amount} carry operations\n"
    return carry_list[:-1]

def ok(s):
    a, b = s.split()
    a, b = a[::-1], b[::-1]
    d = 0
    c = 0
    for i,j in zip(a,b):
        if (int(i)+int(j)+c)>9:
            c=1
            d+=1
        else:
            c=0
    return "{} carry operations".format(d) if d>0 else "No carry operation"
def solve2(s):
    return '\n'.join(ok(i) for i in s.split('\n'))



print(solve("123 456\n555 555\n123 594"))
print(solve("1 9\n123456789 111111101\n01 09\n11 09\n123 457"))


def move_zeros(lst):
    length = len(lst)
    i = length
    while i > 0:
        swap = False
        j = 0
        while j < i-1:
            if lst[j] == 0 and lst[j+1] != 0:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swap = True
            j+=1
        if not swap:
            break
        i -= 1
    return lst


print(move_zeros(
        [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))
print(move_zeros(
    [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))


def snail(snail_map):
    if not snail_map[0]:
        return []
    print(snail_map)
    depth = len(snail_map)
    width = len(snail_map[0])
    size = depth*width
    start_hor = 0
    start_ver = 0
    result = []
    i = 0
    j = 0

    while start_hor < width and start_ver < depth:
        i = start_ver
        j = start_hor
        while j < width-1:
            result.append(snail_map[i][j])
            j += 1
        width -= 1
        while i < depth-1:
            result.append(snail_map[i][j])
            i += 1
        depth -= 1
        while j > start_hor:
            result.append(snail_map[i][j])
            j -= 1
        start_hor += 1
        while i > start_ver:
            result.append(snail_map[i][j])
            i -= 1
        start_ver += 1
    if len(result) > size:
        result = result[::-1]
    elif len(result) < size:
        result.append(snail_map[i][j])
    return result



array = [[1,2,3],
         [4,5,6],
         [7,8,9]]

array2= [[286, 734, 505, 672],
        [901, 161, 705, 899],
        [548, 177, 581, 659],
        [270, 250, 844, 151]]

array3 = [[122, 81, 822, 155, 391, 442],
          [375, 514, 730, 35, 267, 13],
          [462, 717, 898, 96, 638, 348],
          [731, 484, 743, 14, 139, 576],
          [109, 312, 500, 837, 847, 854],
          [138, 175, 296, 16, 999, 285]]

array4 = [[279, 728, 190, 585, 636, 779, 45, 563, 160],
          [50, 331, 621, 448, 149, 571, 968, 365, 215],
          [604, 764, 554, 845, 96, 401, 631, 175, 927],
          [167, 654, 644, 353, 709, 227, 881, 573, 252],
          [429, 487, 970, 242, 359, 291, 614, 168, 616],
          [648, 570, 655, 652, 745, 238, 798, 257, 489],
          [816, 713, 879, 393, 385, 108, 558, 517, 15],
          [661, 75, 83, 551, 947, 467, 501, 416, 69],
          [197, 425, 479, 857, 138, 585, 346, 585, 369]]

print(snail(array))
print(snail(array2))
print(snail(array3))
print(snail([[]]))

"""
[237, 962, 690, 293, 837, 61, 353, 671, 169, 378, 227, 752, 555, 650, 251, 655, 873, 794, 175, 162, 474, 483, 946, 76, 544, 474, 813, 823, 215, 516, 484, 537, 983, 389, 219, 772, 983]
should equal
[237, 962, 690, 293, 837, 61, 353, 671, 169, 378, 227, 752, 555, 650, 251, 655, 873, 794, 175, 162, 474, 483, 946, 76, 544, 474, 813, 823, 215, 516, 484, 537, 983, 389, 219, 772]

[286, 734, 505, 672, 899, 659, 151, 844, 250, 270, 548, 901, 161, 705, 581, 177, 581]
should equal
[286, 734, 505, 672, 899, 659, 151, 844, 250, 270, 548, 901, 161, 705, 581, 177]

[122, 81, 822, 155, 391, 442, 13, 348, 576, 854, 285, 999, 16, 296, 175, 138, 109, 731, 462, 375, 514, 730, 35, 267, 638, 139, 847, 837, 500, 312, 484, 717, 898, 96, 14, 743, 14]
 should equal 
 [122, 81, 822, 155, 391, 442, 13, 348, 576, 854, 285, 999, 16, 296, 175, 138, 109, 731, 462, 375, 514, 730, 35, 267, 638, 139, 847, 837, 500, 312, 484, 717, 898, 96, 14, 743]


[279, 728, 190, 585, 636, 779, 45, 563, 160, 215, 927, 252, 616, 489, 15, 69, 369, 585, 346, 585, 138, 857, 479, 425, 197, 661, 816, 648, 429, 167, 604, 50, 331, 621, 448, 149, 571, 968, 365, 175, 573, 168, 257, 517, 416, 501, 467, 947, 551, 83, 75, 713, 570, 487, 654, 764, 554, 845, 96, 401, 631, 881, 614, 798, 558, 108, 385, 393, 879, 655, 970, 644, 353, 709, 227, 291, 238, 745, 652, 242] 
should equal 
[279, 728, 190, 585, 636, 779, 45, 563, 160, 215, 927, 252, 616, 489, 15, 69, 369, 585, 346, 585, 138, 857, 479, 425, 197, 661, 816, 648, 429, 167, 604, 50, 331, 621, 448, 149, 571, 968, 365, 175, 573, 168, 257, 517, 416, 501, 467, 947, 551, 83, 75, 713, 570, 487, 654, 764, 554, 845, 96, 401, 631, 881, 614, 798, 558, 108, 385, 393, 879, 655, 970, 644, 353, 709, 227, 291, 238, 745, 652, 242, 359]


[286, 734, 505, 672],
[901, 161, 705, 899],
[548, 177, 581, 659],
[270, 250, 844, 151]]
"""

























