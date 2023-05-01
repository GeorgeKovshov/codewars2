import collections

Item = collections.namedtuple('Item', 'weight price')
store = [
  Item(weight=2, price=6),
  Item(weight=2, price=3),
  Item(weight=6, price=5),
  Item(weight=0, price=5),
  Item(weight=5, price=4),
  Item(weight=4, price=6),
  Item(weight=10, price=20),
  Item(weight=0, price=2)
]

store23 = [
  Item(weight=2, price=6),
  Item(weight=2, price=3),
  Item(weight=6, price=5),
  Item(weight=5, price=4),
  Item(weight=4, price=6),
  Item(weight=10, price=20),
]


def greedy_thief1(items, n:int):
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


def greedy_thief2(items, n:int):
    ordered_items = sorted(items, key=lambda x: x.price, reverse=True)
    length = len(ordered_items)
    max_sum = 0
    max_bag = []
    i = 0
    while i < length:
        if ordered_items[i].weight <= n:
            weight = n - ordered_items[i].weight
            sum = ordered_items[i].price
            bag = [ordered_items[i]]
            if sum > max_sum:
                max_bag = bag
                max_sum = sum
            j = i+1
            while j < length:
                if weight - ordered_items[j].weight >= 0:
                    sum += ordered_items[j].price
                    bag.append(ordered_items[j])
                    weight -= ordered_items[j].weight
                    if sum > max_sum:
                        max_bag = bag
                        max_sum = sum
                j += 1
        i += 1
    print(max_sum)
    return max_bag

def check10(item):
    if item.weight == 0:
        return 9999
    elif item.price == 0:
        return -9999
    else:
        return item.price/item.weight


def check2(item):
    if item.weight == 0:
        return 9999
    if item.price == 0:
        return -9999
    else:
        sum = item.price-item.weight
        if sum>=0:
            return sum * (item.price/item.weight)
        elif sum<0:
            return sum * (item.weight/item.price)

"""
def double_check(thief_bag, store):
    for item in store:
        if item not in thief_bag:
            n = len(thief_bag)-1
            while n>=0:
                sum = thief_bag(n)
                while
                    """


def initial_thieving0(items, n:int):
    ordered_dict = sorted(items, key=lambda zt: check1(zt), reverse=True)
    print("new:", ordered_dict)
    thief_bag = []
    sum = 0
    for item in ordered_dict:
        if item.weight <= n:
            n -= item.weight
            thief_bag.append(item)
            sum += item.price
        if n<1:
            break
    return thief_bag








llist = [(1,2), (1,3), (2,4),(1,1), (3,2)]

print(llist[2:])
print(llist[:2])
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

def check1(item):
    if item.weight == 0:
        return 9999
    elif item.price == 0:
        return -9999
    else:
        return item.price/item.weight

def initial_thieving(items, n:int):
    ordered_dict = sorted(items, key=lambda zt: (check1(zt),zt.weight), reverse=True)
    print("new:", ordered_dict)
    thief_bag = []
    remaining_items = []
    sum = 0
    ind = 0
    while ind < len(ordered_dict):
        item = ordered_dict[ind]
        if item.weight <= n:
            n -= item.weight
            thief_bag.append(item)
            sum += item.price
        else:
            remaining_items.append(item)
        if n<1:
            break
        ind += 1
    return [thief_bag, remaining_items, n]


def permutate(lst, n):
    length = len(lst)
    if isinstance(lst[0], Item):
        return lst
    else:
        count = len(lst[0])
    if count == n:
        return lst
    i = length-1
    result = []
    while i>0:
        if not isinstance(lst[i], Item):
            i += 1
            break
        i -= 1
    end = i
    used_ints = []
    while i < length:
        j = 0
        used_ints.append(lst[i])
        while not isinstance(lst[j], Item) and lst[j][0] in used_ints:
            j += 1
        while j < end and len(lst[j]) == count:
            result.append([lst[i]] + lst[j])
            j += 1
        i+=1
    return permutate(result + lst, n)



def permute(lst):

    #print("permuting:", lst)
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


def recombobulate(thief_bag, new_item, old_items):
    return [item for item in thief_bag if item not in old_items] + [new_item]


def be_greedy(thief_bag, combo_bag, remaining_items, weight, max_weight):
    greed_sated = True
    i = 0
    while i < len(remaining_items) and greed_sated:
    #for store_item in remaining_items:
        store_item = remaining_items[i]
        j = 0
        while j<len(combo_bag):
        #for combo in combo_bag:
            summ_price = 0
            summ_weight = 0
            #print("combo_bag:", combo_bag[j])
            first = True
            for x in combo_bag[j]:
                if isinstance(x,int) and first:
                    summ_weight += x
                    first = False
                elif isinstance(x,int) and not first:
                    summ_price += x
                else:
                    summ_price += x.price
                    summ_weight += x.weight
            if store_item.price > summ_price and store_item.weight <= summ_weight+weight:
                thief_bag = recombobulate(thief_bag, remaining_items[i], combo_bag[j])
                weight = 0
                for item in thief_bag:
                    weight += item.weight
                weight = max_weight - weight
                try:
                    remaining_items = remaining_items[:i] + combo_bag[j] + remaining_items[i+1:]
                except:
                    remaining_items = remaining_items[:i] + [combo_bag[j]] + remaining_items[i + 1:]
                combo_bag = permute(thief_bag)
                greed_sated = False
                break
            j += 1
        i += 1
    if greed_sated:
        return thief_bag
    else:
        print("combo",combo_bag)
        return be_greedy(thief_bag, combo_bag, remaining_items, weight, max_weight)






def greedy_thief145(items, n:int):
    thief_bag, remaining_items, weight = initial_thieving(items, n)
    combo_bag = permute(thief_bag)
    print(thief_bag)
    #for x in combo_bag:
    #    print(x)
    return be_greedy(thief_bag, combo_bag, remaining_items, weight, n)


store2 = [
          Item(weight=2, price=6),
          Item(weight=2, price=3),
          Item(weight=6, price=5),
          Item(weight=5, price=4),
          Item(weight=4, price=6),
]
#print(greedy_thief(store2,10))



#print(greedy_thief(store, 10))
#print("recombobulation")
#print(recombobulate([1,2,3,4,5,6,7,8], 10, [3,4,5]))


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


def recursive_thief_original(items, n):
    length = len(items)
    if length == 0:
        return 0
    elif length < 1:
        if n - items.weight >= 0:
            return items.price
        else:
            return 0
    max_price = 0
    ind = 0
    while ind<length:
        if items[ind].weight <= n:
            sum_price = items[ind].price + recursive_thief_original(items[ind+1:], n - items[ind].weight)
            if sum_price>max_price:
                max_price = sum_price
        else:
            break
        ind+=1
    return max_price


def recursive_thief_good_but_slow(items, n):
    length = len(items)
    if length == 0:
        return 0, []
    elif length < 1:
        if n - items.weight >= 0:
            return items.price, [items]
        else:
            return 0
    max_thief_bag = []
    max_price = 0
    ind = 0
    while ind < length:
        sum_price1, thief_bag1 = recursive_thief(items[ind + 1:], n)
        if items[ind].weight <= n:
            sum_price, thief_bag = recursive_thief(items[ind + 1:], n - items[ind].weight)
            sum_price += items[ind].price
            thief_bag.append(items[ind])
            if sum_price > max_price:
                max_price = sum_price
                max_thief_bag = thief_bag
        if sum_price1 > max_price:
            max_price = sum_price1
            max_thief_bag = thief_bag1
        else:
            break
        ind += 1
    return max_price, max_thief_bag


def recursive_thief233(items, n):
    length = len(items)
    if length == 0:
        return 0, []
    elif length < 1:
        if n - items.weight >= 0:
            return 0, []
        else:
            return 0
    max_thief_bag = []
    max_price = 0
    ind = 0
    while ind < length:
        #sum_price1, thief_bag1, sum_price, thief_bag = recursive_thief(items[ind + 1:], n)
        if items[ind].weight <= n:
            sum_price, thief_bag = recursive_thief(items[ind + 1:], n - items[ind].weight)
            sum_price += items[ind].price
            thief_bag.append(items[ind])
            if sum_price > max_price:
                max_price = sum_price
                max_thief_bag = thief_bag
        ind += 1
    return max_price, max_thief_bag

def recursive_thief(items, n):
    length = len(items)
    if length == 0:
        return 0, []
    elif length < 1:
        if n - items.weight >= 0:
            return items.price, [items]
        else:
            return 0
    max_thief_bag = []
    max_price = 0
    sum_price, thief_bag = recursive_thief(items[1:], n - items[0].weight)
    if items[0].weight <= n:
        sum_price += items[0].price
        thief_bag.append(items[0])
    if sum_price > max_price:
        max_price = sum_price
        max_thief_bag = thief_bag

    return max_price, max_thief_bag

def big_loop(items, n):
    length = len(items)
    max_thief_bag = []
    max_price = 0

    ind = 0
    while ind < length:
        sum_price, thief_bag = recursive_thief(items[ind + 1:], n- items[ind].weight)
        if items[ind].weight <= n:
            sum_price1, thief_bag1 = recursive_thief(items[ind + 1:], n - items[ind].weight)
            sum_price1 += items[ind].price
            thief_bag1.append(items[ind])
            if sum_price1 > max_price:
                max_price = sum_price1
                max_thief_bag = thief_bag1
        if sum_price > max_price:
            max_price = sum_price
            max_thief_bag = thief_bag
        ind += 1
    return max_price, max_thief_bag



def greedy_thief(items,n):
    ordered_items = sorted(items, key=lambda x: (-x.weight, -x.price))
    print(ordered_items)
    zeros = len(ordered_items)-1
    if ordered_items[zeros].weight>n:
        return []
    while ordered_items[zeros].weight == 0 and zeros>0:
        zeros -= 1
    if zeros == 0 and ordered_items[0].weight == 0:
        return ordered_items
    else:
        result = big_loop(ordered_items[:zeros+1], n)
        """
        print(result[1])
        print(result[0])
        """
        sum = 0
        for x in ordered_items[zeros+1:]:
            sum+=x.price

        return result[0] + sum

#print(store)
store3 =[
    Item(weight=1, price=22),
    Item(weight=0, price=33)
]

print(greedy_thief(store, 12))
nums1 = [-2,1,-3,4,-1,2,1,-5,4]
big_store = [
    Item(weight=30, price=34),
    Item(weight=30, price=24),
    Item(weight=30, price=23),
    Item(weight=30, price=11),
    Item(weight=29, price=38),
    Item(weight=28, price=37),
    Item(weight=28, price=1),
    Item(weight=26, price=37),
    Item(weight=26, price=31),
    Item(weight=25, price=16),
    Item(weight=24, price=49),
    Item(weight=24, price=21),
    Item(weight=21, price=48),
    Item(weight=21, price=48),
    Item(weight=21, price=3),
    Item(weight=19, price=46),
    Item(weight=18, price=13),
    Item(weight=17, price=40),
    Item(weight=16, price=41),
    Item(weight=16, price=33),
    Item(weight=15, price=47),
    Item(weight=15, price=35),
    Item(weight=14, price=14),
    Item(weight=13, price=25),
    Item(weight=13, price=22),
    Item(weight=13, price=21),
    Item(weight=13, price=4),
    Item(weight=12, price=36),
    Item(weight=12, price=36),
    Item(weight=12, price=4),
    Item(weight=12, price=2),
    Item(weight=10, price=19),
    Item(weight=9, price=3),
    Item(weight=8, price=43),
    Item(weight=7, price=11),
    Item(weight=7, price=0),
    Item(weight=6, price=46),
    Item(weight=5, price=31),
    Item(weight=5, price=23),
    Item(weight=4, price=35),
    Item(weight=3, price=27),
    Item(weight=3, price=15),
    Item(weight=3, price=10),
    Item(weight=2, price=30),
    Item(weight=2, price=26),
    Item(weight=1, price=41),
    Item(weight=0, price=41),
    Item(weight=0, price=40),
    Item(weight=0, price=37),
    Item(weight=0, price=21),
    Item(weight=0, price=3)
]

#print(greedy_thief(big_store, 372))
#print(recursive_thief(nums1))

#print(recursive_thief([1,2,3,-4,5,6,7,8]))










