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

#print(snail(array))
#print(snail(array2))
#print(snail(array3))
#print(snail([[]]))

prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
              101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
              211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293,
              307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397,
              401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499]

def check_prime(num):
    if num > 1:
        # Iterate from 2 to n / 2
        for i in range(2, int(num / 2) + 1):
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False

def simplified_array(a):
    if len(a)<=1:
        return a
    if a[0] in prime_list:
        is_prime = 1
    elif a[0] not in prime_list:
        is_prime = -1
    else:
        return []
    result = []
    summ = 0
    for x in a:
        if x > 499:
            if check_prime(x) and x not in prime_list:
                prime_list.append(x)
        if is_prime == 1:
            if x in prime_list:
                summ += x
            else:
                result.append(summ)
                summ = x
                is_prime *= -1
        elif is_prime == -1:
            if x not in prime_list:
                summ += x
            else:
                result.append(summ)
                summ = x
                is_prime *= -1
    result.append(summ)
    if len(result) == len(a):
        return result
    else:
        return simplified_array(result)

print(simplified_array([1, 2, 3, 5, 6, 4, 2, 3]))

"""
from gmpy2 import is_prime
from itertools import groupby

def simplified_array(xs):
    while len(xs) != len(xs := [sum(g) for _, g in groupby(xs, lambda x: x > 0 and is_prime(x))]):
        pass
    return xs
"""



import collections

Item = collections.namedtuple('Item', 'weight price')
store = [
  Item(weight=2, price=6),
  Item(weight=2, price=3),
  Item(weight=6, price=5),
  Item(weight=5, price=4),
  Item(weight=4, price=6),
  Item(weight=10, price=20)
]


def greedy_thief(items, n:int):
    list_items = []
    for x in items:
        #print(x, "valuability: ", x.price/x.weight)
        if x.weight != 0:
            list_items.append((x, x.price / x.weight))
        else:
            list_items.append((x, 9999))
    ordered_dict = sorted(list_items, key=lambda y:(y[1],-y[0].weight), reverse=True) # -y[0] - it reverses the sorting
    thief_bag = []
    item_index = 0
    for item in ordered_dict:
        print(item)
        if item[0].weight<=n:
            n -= item[0].weight
            thief_bag.append(item[0])
        item_index += 1
        if n<1:
            break
        #print(item[0])
        #print(item[0].weight)
    reverse_index = len(ordered_dict) - 1
    lightest_item = [9999, 9999]
    light_item_ind = -1
    for ind, z in enumerate(thief_bag):
        print("thief bag ", ind, z)
        if z.weight<lightest_item[0] or (z.weight==lightest_item[0] and z.price<lightest_item[1]):
            lightest_item = [z.weight, z.price]
            light_item_ind = ind

    print(light_item_ind)
    if n >= 1 and thief_bag:
        for item in reversed(ordered_dict):
            if item[0].weight - thief_bag[light_item_ind].weight <= n and item[0].price > thief_bag[light_item_ind].price:
                thief_bag[light_item_ind] = item[0]
                n -= item[0].weight - thief_bag[light_item_ind].weight
            reverse_index -= 1
            if n < 1 or reverse_index <= item_index:
                break

    print("result")
    return thief_bag


#print(greedy_thief(store, 5))


llist = [(1,2), (1,3), (2,4),(1,1), (3,2)]
#llist.sort(key=lambda y:y[1])
#print(llist)

"""
Test: n=41, max price is 69
Log
(Item(weight=10, price=22), 2.2)
(Item(weight=14, price=28), 2.0)
(Item(weight=28, price=47), 1.6785714285714286)
(Item(weight=22, price=11), 0.5)
(Item(weight=17, price=6), 0.35294117647058826)
result
You should get the max possible price: 56 should be 69

Test: n=66, max price is 92
Log
(Item(weight=26, price=44), 1.6923076923076923)
(Item(weight=16, price=26), 1.625)
(Item(weight=28, price=29), 1.0357142857142858)
(Item(weight=22, price=21), 0.9545454545454546)
(Item(weight=24, price=22), 0.9166666666666666)
thief bag  0 Item(weight=26, price=44)
thief bag  1 Item(weight=16, price=26)
thief bag  2 Item(weight=22, price=21)
1
result
You should get the max possible price: 91 should be 92


"""
#print(llist[:2])

def subarray(lst):
    length = len(lst)
    if length == 0:
        return 0
    elif length == 1:
        return lst[0]
    elif length == 2:
        return max(lst[0], lst[1], lst[0] + lst[1])
    if lst[0]>0:
        sum = lst[0]
    else:
        sum = 0
    sum2 = lst[0]
    max_sum = -1000000
    highest_negative = 1
    neg_sum = 0
    i = 1
    while i < length:
        sum += neg_sum
        neg_sum = 0
        if sum+lst[i] > sum:
            sum += lst[i]
            sum2 += lst[i]
            i += 1
        elif lst[i] <= 0:
            while i < length and lst[i] <= 0:
                neg_sum += lst[i]
                if lst[i] > highest_negative or highest_negative>0:
                    highest_negative = lst[i]
                i += 1
            sum2=0
        else:
            if lst[i]>0:
                sum = lst[i]
            i += 1
        if sum2>sum and sum2!=0:
            sum = sum2
        if sum > max_sum:
            max_sum = sum
    if max_sum == 0 and highest_negative>0:
        return 0
    elif max_sum>0:
        return max_sum
    else:
        return highest_negative

def subarray2(nums):
    newNum = maxTotal = nums[0]

    for i in range(1, len(nums)):
        newNum = max(nums[i], nums[i] + newNum)
        maxTotal = max(newNum, maxTotal)

    return maxTotal



#nums4=[-1, 0, -2]
#nums2 = [-2,-3,-1]
#nums3=[0,0,0,0,0]
#nums = [5,4,-1,7,8]
#nums1 = [-2,1,-3,4,-1,2,1,-5,4]
#length=len(nums)
#print(nums[(length//2-length//4):(length//2+length//4)])

#print(nums[:4])
#print(nums[:length//2])
#print(nums[length//2:])
#print(subarray2(nums1))
#print(max(3,2,1,3))

def is_divided_by_three(var):
    if var == 0:
        return False
    y = var
    sum = 0
    while y >= 1:
        sum += y % 10
        y = y // 10
    if sum >= 10:
        return is_divided_by_three(sum)
    elif sum % 3 == 0:
        return True
    else:
        return False

def solution1(number):
    if number <= 0:
        return 0
    nums = []
    for x in range(number):
        if x!=0 and (x % 5 == 0 or x % 10 == 0):
            nums.append(x)
        elif is_divided_by_three(x):
            nums.append(x)
    sum = 0
    for y in nums:
        sum += y
    return sum


def solution2(number):
    if number <= 0:
        return 0
    cycle2 = {}
    cycle = [3, 2, 1, 3, 1, 2, 3, 3, 2, 1, 3, 1, 2, 3]
    for i in range(14):
        cycle2[i]=cycle[i]
    var = 0
    summ = 0
    i = 0
    length = len(cycle)
    print(length)
    while var < number:
        summ += var
        var += cycle2[i]
        if i == length - 1:
            i = 0
        else:
            i += 1

    return summ

def solution3(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)

def solution4(number):
    a3 = (number-1)/3
    a5 = (number-1)/5
    a15 = (number-1)/15
    result = (a3*(a3+1)/2)*3 + (a5*(a5+1)/2)*5 - (a15*(a15+1)/2)*15
    return result

import time
#start_time = time.time()
#print(solution2(12311233))
#end_time = time.time()
#elapsed_time = end_time - start_time
#print("Elapsed time: ", elapsed_time)


def max_sum_of_n(n, lst):
    i = 0
    max_sum = 0
    list_max = []
    while i<n:
        max_int = -9999
        max_ind = -1
        for ind, x in enumerate(lst):
            if x > max_int and ind not in list_max:
                max_int = x
                max_ind = ind
        max_sum += max_int
        list_max.append(max_ind)
        i += 1
    return max_sum

#n = int(input("number of numbers:"))

#print(max_sum_of_n(n,[-2,1,-3,4,-1,2,1,-5,4]))

def permutate2(lst):
    length = len(lst)
    if length == 1:
        return [lst]
    result = []
    for ind, item in enumerate(lst):
        i = ind+1
        while i < length:
            result.append([item, lst[i]])
            i += 1
    return result


def permutate1(lst):
    length = len(lst)
    i = 0
    result = []
    while i<length:
        j = i + 1
        while j < length:
            result.append([lst[i],lst[j]])
            j += 1
        i+=1
    return lst + result

def permutate_prototype(lst):
    length = len(lst)
    if length==1:
        return lst
    if not isinstance(lst[0],int):
        count = len(lst[0])
        if len(lst[0]) == 4:
            return lst
    i = length-1
    result = []
    first = True
    while i>0:
        if not isinstance(lst[i],int):
            first = False
            i += 1
            break
        i -= 1
    end = i
    used_ints = []
    while i < length:
        if first:
            j = i + 1
            while j < length:
                result.append([lst[i], lst[j]])
                j += 1
        else:
            j = 0
            used_ints.append(lst[i])
            while not isinstance(lst[j],int) and lst[j][0] in used_ints:
                j += 1
            while j < end and len(lst[j]) == count:
                result.append([lst[i]] + lst[j])
                j += 1

        i+=1
    return permutate(result + lst)


def permutate(lst, n):
    length = len(lst)
    if isinstance(lst[0],int):
        return lst
    else:
        count = len(lst[0])
    if count == n:
        return lst
    i = length-1
    result = []
    while i>0:
        if not isinstance(lst[i],int):
            i += 1
            break
        i -= 1
    end = i
    used_ints = []
    while i < length:
        j = 0
        used_ints.append(lst[i])
        while not isinstance(lst[j],int) and lst[j][0] in used_ints:
            j += 1
        while j < end and len(lst[j]) == count:
            result.append([lst[i]] + lst[j])
            j += 1
        i+=1
    return permutate(result + lst, n)


list = [1,2,3,4,5]
def permute(lst):
    length = len(lst)
    if length == 1:
        return lst
    if length == 2:
        return [[lst[0],lst[1]], lst[0], lst[1]]
    result = []
    for i, x in enumerate(lst):
        j = i + 1
        while j < length:
            result.append([lst[i], lst[j]])
            j += 1
    return permutate(result + lst, length)

#print(permute(list))
#print([2]+list)
llist = permute(list)
for item in llist:
    print(item)
list = [1,2,3,4,5,6,7]
print(list[3:])


def recursive_max_sum(remaining_items):
    length = len(remaining_items)
    if length == 0:
        return 0
    elif length < 1:
        return remaining_items
    max = 0
    ind = 0

    while ind < length:
        #print(remaining_items[ind + 1])
        sum = remaining_items[ind] + recursive_max_sum(remaining_items[ind+1:])
        if sum>max:
            max = sum
        ind += 1
    return max





























