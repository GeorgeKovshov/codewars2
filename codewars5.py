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
        """
        val = self.collection[item_index]
        for ind, x in enumerate(self.collection_pages):
            if val in x:
                return ind
        return -1
        """


helper = PaginationHelper(['a','b','c','d','e','f'], 4)
print(helper.collection_pages)

print(helper.page_index(5))



























