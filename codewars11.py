arr = [
    [1,2,3,4,5],
    [2,3,4,5,6],
    [9,8,7,6,5],
    [5,2,3,5]
]

#for a in arr:
#    del(a[a.index(5)])

#print(arr)


def runoff_CORRECT(voters):
    candidates = {}
    for v in voters:
        voting_preference = len(v)
        for c in v:
            if c not in candidates:
                candidates[c] = 0
            candidates[c] += voting_preference
            voting_preference -= 1
    while candidates:
        if len(candidates) == 1:
            for x in candidates:
                return x
        print(candidates)
        min_c = [[10000, ""]]
        max_c = [[-1, ""]]
        total_votes = 0
        for c in candidates:
            if candidates[c] < min_c[0][0]:
                min_c = [[candidates[c], c]]
            elif candidates[c] > max_c[0][0]:
                max_c = [[candidates[c], c]]
            elif candidates[c] == min_c[0][0]:
                min_c.append([candidates[c], c])
            elif candidates[c] == max_c[0][0]:
                max_c = [[candidates[c], c]]
            total_votes += candidates[c]
        print("min", min_c)
        print("max", max_c)
        if min_c[0][1] == max_c[0][1]:
            return None
        if min_c[0][1] != "":
            for m in min_c:
                del (candidates[m[1]])
        if max_c[0][0] > total_votes // 2 and len(max_c) == 1:
            return max_c[0][1]
        # candidates = {}
        for c in candidates:
            candidates[c] = 0
        for v in voters:
            # for m in min_c:
            #    if m[1] in v:
            #        del(v[v.index(m[1])])
            voting_preference = len(v)
            for c in v:
                if c in candidates:
                    candidates[c] += voting_preference
                voting_preference -= 1
            reserve = 0
    return None


def runoff(voters):
    candidates = {}
    for v in voters:
        voting_preference = len(v)
        for c in v:
            if c not in candidates:
                candidates[c] = 0
            candidates[c] += voting_preference
            voting_preference -= 1
    while candidates:
        if len(candidates) == 1:
            for x in candidates:
                return x
        print(candidates)
        min_c = [[10000, ""]]
        max_c = [[-1, ""]]
        total_votes = 0
        for c in candidates:
            if candidates[c] < min_c[0][0]:
                min_c = [[candidates[c], c]]
            elif candidates[c] > max_c[0][0]:
                max_c = [[candidates[c], c]]
            elif candidates[c] == min_c[0][0]:
                min_c.append([candidates[c], c])
            elif candidates[c] == max_c[0][0]:
                max_c = [[candidates[c], c]]
            total_votes += candidates[c]
        print("min", min_c)
        print("max", max_c)
        if min_c[0][1] == max_c[0][1]:
            return None
        if min_c[0][1] != "":
            for m in min_c:
                del (candidates[m[1]])
        if max_c[0][0] > total_votes // 2 and len(max_c) == 1:
            return max_c[0][1]
        # candidates = {}
        for c in candidates:
            candidates[c] = 0
        for v in voters:
            # for m in min_c:
            #    if m[1] in v:
            #        del(v[v.index(m[1])])
            voting_preference = len(v)
            reserve = 0
            i = len(c) - 1
            while i >= 0:
                if v[i] not in candidates:
                    reserve += voting_preference
                else:
                    candidates[v[i]] += voting_preference
                voting_preference -= 1
                i -= 1
            i = 0
            while reserve > 0:
                if i > len(v):
                    i = 0
                if v[i] not in candidates:
                    continue
                else:
                    candidates[v[i]] += 1
                reserve -= 1
    return None


voters = [["dem", "ind", "rep"],
                  ["rep", "ind", "dem"],
                  ["ind", "dem", "rep"],
                  ["ind", "rep", "dem"]]


def runoff(voters):
    candidates = {}
    max_c = [[0, ""]]
    min_c = [[10000, ""]]

    for v in voters:
        if v[0] not in candidates:
            candidates[v[0]] = 0
    while candidates:
        if len(candidates) == 1:
            for x in candidates:
                return x
        max_c = [[0, ""]]
        min_c = [[10000, ""]]
        for v in voters:
            i = 0
            while i < len(v) and v[i] not in candidates:
                i += 1
            if i >= len(v):
                continue
            if v[i] in candidates:
                candidates[v[i]] += 1

        mini = 10000
        maxi = 0
        for c in candidates:
            if candidates[c] < mini:
                mini = candidates[c]
            if candidates[c] > maxi:
                maxi = candidates[c]
        minimal = []
        for c in candidates:
            if candidates[c] == mini:
                minimal.append(c)
        for m in minimal:
            del (candidates[m])
        for c in candidates:
            if candidates[c] == maxi and maxi > len(voters) // 2:
                return c


    return None

#print(runoff(voters))


def longest_sequence(arr, command):
    com_inc = True if command in ["<<", "< <"] else False
    prev = arr[0]
    max_window = [0,0]
    window = [0,0]
    if com_inc:
        for i in range(len(arr)):
            if arr[i] > prev:
                window[1] = i
            elif arr[i] <= prev:
                window[0] = i
                window[1] = i
            max_window = window if (window[1] - window[0]) > (max_window[1] - max_window[0]) else max_window
            prev = arr[i]
    else:
        for i in range(len(arr)):
            if arr[i] < prev:
                window[1] = i
            elif arr[i] >= prev:
                window[0] = i
                window[1] = i
            max_window = window if (window[1] - window[0]) > (max_window[1] - max_window[0]) else max_window
            prev = arr[i]
    return max_window if (max_window[1] - max_window[0]) > 2 else []



def longest_comb_1(arr, command):
    com_inc_lam = lambda a, b: a > b if command in ["<<", "< <"] else a < b
    max_window = 0
    list_comb = []
    for i in range(len(arr)):
        list_cur = [arr[i]]
        prev = arr[i]
        count = 0
        for j in range(i, len(arr)):
            if com_inc_lam(arr[j], prev):
                count += 1
                list_cur.append(arr[j])
                prev = arr[j]
        if count > max_window:
            max_window = count
            list_comb = [list_cur]
        elif count == max_window:
            list_comb.append(list_cur)
    if max_window < 2:
        return []
    elif max_window == len(arr):
        return arr
    return list_comb if len(list_comb) > 1 else list_comb[0]


class Long_comb:

    def __init__(self, command):
        self.com_inc_lam = lambda a, b: a > b if command in ["<<", "< <"] else a < b
        self.result = []
        self.max_count = 0

    def rec_comb(self, arr, i, prev, count):
        if count > self.max_count:
            self.result = [prev]
            self.max_count = count
        elif count == self.max_count and prev not in self.result:
            self.result.append(prev)
        if i >= len(arr):
            return count
        rec1 = 0

        if self.com_inc_lam(arr[i], prev[-1]):
            rec1 = self.rec_comb(arr, i + 1, list(prev) + [arr[i]], count + 1)

        rec3 = self.rec_comb(arr, i + 1, list(prev), count)
        rec2 = self.rec_comb(arr, i + 1, [arr[i]], 1)
        return

    def longest_comb(self, arr):
        self.rec_comb(arr, 1, [arr[0]], 1)
        if self.max_count < 3:
            return []
        if len(self.result) == 1:
            return self.result[0]
        return self.result


def longest_comb_true(arr, command):
    if len(arr) == 0:
        return []
    comb = Long_comb(command)
    return comb.longest_comb(arr)


class Long_comb2:

    def __init__(self, command):
        self.com_inc_lam = lambda a, b: a > b if command in ["<<", "< <"] else a < b
        self.result = []
        self.max_count = 0

    def rec_comb(self, arr, i, prev, count):
        if i >= len(arr):
            return count
        rec1 = 0
        rec3 = self.rec_comb(arr, i + 1, list(prev), count)
        if not prev:
            rec1 = self.rec_comb(arr, i + 1, list(prev) + [arr[i]], count + 1)
        elif self.com_inc_lam(arr[i], prev[-1]):
            if count + 1 > self.max_count:
                self.result = [prev + [arr[i]]]
                self.max_count = count + 1
            elif count + 1 == self.max_count:
                self.result.append(prev + [arr[i]])
            rec1 = self.rec_comb(arr, i + 1, list(prev) + [arr[i]], count + 1)

        # rec2 = self.rec_comb(arr, i+1, [arr[i]], 1)
        return

    def longest_comb(self, arr):
        self.rec_comb(arr, 0, [], 0)
        # self.rec_comb(arr, 1, [arr[0]], 1)
        if self.max_count < 3:
            return []
        if len(self.result) == 1:
            return self.result[0][::-1]
        return self.result


def longest_comb2(arr, command):
    if len(arr) == 0:
        return []
    comb = Long_comb2(command)
    return comb.longest_comb(arr)[::-1]


def smallest_possible_reduction_sum(a):
    a.sort()
    i = 0
    while i < len(a) - 1:
        if a[i] == 1:
            return len(a)
        while a[i] != a[i+1]:
            if a[i] > a[i+1]:
                a[i] = a[i+1] if a[i] % a[i+1] == 0 else a[i] % a[i+1]
            elif a[i] < a[i+1]:
                a[i+1] = a[i] if a[i+1] % a[i] == 0 else a[i+1] % a[i]
        i += 1
    return a[-1] * len(a)
"""
arr = [1, 2, 23, 4, 5, 9]
a = arr[:1] + arr[1:5][::-1] + arr[5:]
print(arr)
print(a)
for i in range(22, 28):
    print(i)

arr = [x if x % 2 == 0 else 0 for x in arr]
print(arr)"""

def paren_rec2(string, i, end):
    start = i
    check = False
    new_string = string[:i]
    while i < end // 2:
        if string[i] == '(':
            check = True
            new_string += ')'
        elif string[i] == ')':
            new_string += '('
        else:
            new_string += string[end - i]
        i += 1
    while i < end:
        new_string += string[end - i]
        i += 1
    i = start
    if not check:
        return new_string
    stack = 0
    while i < end:
        if new_string[i] == '(':
            if stack == 0:
                start_end[0] = i
            stack += 1
        elif new_string[i] == ')':
            stack -= 1
            if stack == 0:
                stack_end[1] = i
                new_string = new_string[:stack_end[0]] + paren_rec2(new_string, stack_end[0] + 1,
                                                                   stack_end[1]) + new_string[stack_end[1]:]
        i += 1
    return new_string


def reverse_in_parentheses2(string):
    stack = 0
    start_end = [0, 0]
    for i in range(len(string)):
        if string[i] == '(':
            if stack == 0:
                start_end[0] = i
            stack += 1
        elif string[i] == ')':
            stack -= 1
            if stack == 0:
                start_end[1] = i
                string = string[:start_end[0]] + paren_rec2(string, start_end[0] + 1, start_end[1]) + string[
                                                                                                     start_end[1]:]
    return string


def paren_rec(string, j, end):
    stack = 0
    start_end = [[0, 0]]
    for i in range(j, end):
        if string[i] == '(':
            if stack == 0:
                print("starrrr", start_end[-1])
                start_end[-1][0] = i
            stack += 1
        elif string[i] == ')':
            stack -= 1
            if stack == 0:
                start_end[-1][1] = i
                string = paren_rec(string, start_end[-1][0] + 1, start_end[-1][1])
                start_end.append([0, 0])
    print(start_end)
    if start_end[0][1] != 0:
        dict = {
            '(': ')',
            ')': '('
        }
        for pair in start_end:
            if pair == [0,0]:
                break
            parente = "".join([x if x not in ['(', ')'] else dict[x] for x in string[pair[0] + 1:pair[1]][::-1]])
            string = string[:pair[0]] + '(' + parente + ')' + string[pair[1] + 1:]
    return string


def reverse_in_parentheses(string):
    print(string)
    return paren_rec(string, 0, len(string))

#print(reverse_in_parentheses("many (parens) on (pot)"))


#class Proc:
#    def __init__(self, lst):


def divisors_old(num):
    divisor = set()
    divisor.add(1)
    divisor.add(num)
    i = 2
    while i < num // 2:
        if num % i == 0:
            divisor.add(i)
            divisor.add(int(num / i))
        i += 1
    return divisor

def proc_arr_int2(lst):
    divisor_count = [0] * len(lst)
    for i in range(2, max(lst) // 2):
        for j in range(len(lst)):
            if lst[j] % i == 0:
                divisor_count[j] += 1
    maxi = max(divisor_count)
    result = [a for a, b in zip(lst,divisor_count) if b == maxi]
    return [len(lst), divisor_count.count(0), [maxi, result]]


def proc_arr_int1(lst):
    divisor_count = [0] * len(lst)
    for i in range(2, max(lst) // 2):
        for j in range(len(lst)):
            if lst[j] < i:
                continue
            elif lst[j] % i == 0:
                if lst[j] / i == i:
                    divisor_count[j] += 1
                else:
                    divisor_count[j] += 2
    maxi = max(divisor_count)
    print(divisor_count)
    result = [a for a, b in zip(lst,divisor_count) if b == maxi]
    return [len(lst), divisor_count.count(0), [maxi, result]]

def proc_arr_int_slow(lst):
    divisor_count = [0] * len(lst)
    maxi = 0
    for i in range(2, max(lst)):
        for j in range(len(lst)):
            if lst[j] <= i:
                continue
            elif lst[j] % i == 0:
                divisor_count[j] += 1
                maxi = divisor_count[j] if divisor_count[j] > maxi else maxi
    result = [a for a, b in zip(lst,divisor_count) if b == maxi]
    result.sort()
    return [len(lst), divisor_count.count(0), [maxi+2, result]]

def divisors(num):
    if num == 0:
        return 2
    divisor = set()
    divisor.add(1)
    divisor.add(num)
    i = 2
    while i <= int(num**1/2) + 1:
        if num % i == 0:
            divisor.add(i)
            divisor.add(int(num / i))
        i += 1
    return len(divisor)

def proc_arr_int(lst):
    prime_count = 0
    max_count = 0
    result = []
    length = 0
    for x in lst:
        length += 1
        divisor_count = divisors(x)
        if divisor_count <= 2:
            prime_count += 1
        if divisor_count > max_count:
            result = [x]
            max_count = divisor_count
        elif divisor_count == max_count:
            new_result = []
            i = 0
            while result[i] < x:
                new_result.append(result[i])
                i += 1
            new_result.append(x)
            result = new_result + result[i:]
    return [length, prime_count, [max_count, result]]


class Proc:
    def __init__(self):
        self.divisors = set()
        self.prime_count = 0
        self.max_count = 0
        self.primes = [0, 1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

    def get_divisors(self, num):
        divisor = set()
        divisor.add(1)
        divisor.add(num)
        self.divisors.add(num)
        i = 2
        while i <= num // 2:
            if num % i == 0:
                self.divisors.add(i)
                self.divisors.add(int(num / i))
                divisor.add(i)
                divisor.add(int(num / i))
            i += 1
        return len(divisor)

    def proc_arr_int(self, lst):
        result = []
        length = 0
        for x in lst:
            length += 1
            if x in self.primes:
                self.prime_count += 1
                continue
            elif x in self.divisors:
                continue
            divisor_count = self.get_divisors(x)
            if divisor_count <= 2:
                self.primes.add(x)
                self.prime_count += 1
            if divisor_count > self.max_count:
                result = [x]
                self.max_count = divisor_count
            elif divisor_count == self.max_count:
                new_result = []
                i = 0
                while result[i] < x:
                    new_result.append(result[i])
                    i += 1
                new_result.append(x)
                result = new_result + result[i:]
        return [length, self.prime_count, [self.max_count, result]]
"""
result = []
for i in range(1000):
    if divisors(i) <= 2:
        result.append(i)
print(result)"""


#print(proc_arr_int1([36, 98]))
#print([0] * 5)

#print(divisors_old(36))

def crazyRabbit(field, cr):
    cr = field[0]
    i = 0
    dir_right = True
    while cr != 0:
        field[i] = 0
        cr = cr % (len(field) * 2)
        while cr != 0:
            if dir_right:
                if i + cr >= len(field):
                    cr -= len(field) - i + 1
                    i = len(field) - 1
                    dir_right = False
                else:
                    i += cr
                    cr = 0
            if not dir_right:
                if i - cr < 0:
                    cr -= len(field) - i + 1
                    i = 0
                    dir_right = True
                else:
                    i -= cr
                    cr = 0
        cr = field[i]
    return sum(field) == 0

#print(crazyRabbit([1, 0, 1], 0))

def crazyRabbit(field, cr):
    print(field, cr)
    i = cr
    cr = field[i]
    dir_right = True
    visited = {}
    while True:
        cr_old = cr
        field[i] = 0
        cr = cr % (len(field) * 2)
        while cr != 0:
            if dir_right:
                if i + cr >= len(field):
                    cr -= len(field) - i
                    i = len(field) - 1
                    dir_right = False
                else:
                    i += cr
                    cr = 0
            if not dir_right:
                if i - cr < 0:
                    cr -= i + 1
                    i = 0
                    dir_right = True
                else:
                    i -= cr
                    cr = 0
        cr = cr_old + field[i]
        if field[i] == 0:
            if i not in visited:
                visited[i] = 0
            visited[i] += 1
            if visited[i] > 2:
                break
        else:
            visited = {}
    return sum(field) == 0


def first_non_repeating_letter_old(s):
    dict = {}
    for x in s:
        if x.lower() not in dict:
            dict[x.lower()] = [0,0] # [upper, lowercase count]
        if x.isupper():
            dict[x.lower()][0] += 1
        else:
            dict[x.lower()][1] += 1
    mini_id_upper = [len(s)+1, "", True]
    for y in dict:
        if dict[y][0] + dict[y][1] < mini_id_upper[0]:
            mini_id_upper[0] = dict[y][0] + dict[y][1]
            mini_id_upper[1] = y
            mini_id_upper[2] = True if dict[y][0] > dict[y][1] else False
        if dict[y][0] + dict[y][1] > 1:
            mini_id_upper[1] = ""
    return mini_id_upper[1].upper() if mini_id_upper[2] else mini_id_upper[1]


def first_non_repeating_letter(s):
    if not s:
        return ""
    dict = {}
    mini = [len(s) + 1, ""]
    for x in s:
        if x.lower() not in dict:
            dict[x.lower()] = [0, 0]  # [upper, lowercase count]
        if x.isupper():
            dict[x.lower()][0] += 1
        else:
            dict[x.lower()][1] += 1

    for y in dict:
        if dict[y][0] + dict[y][1] < mini[0]:
            mini[0] = dict[y][0] + dict[y][1]
            mini[1] = y

    if mini[0] != 1:
        return ""
    return s[s.lower().find(mini[1])]


print(first_non_repeating_letter("abba"))


def dead_ant_count(ants):
    dict = {
        'a': 0,
        'n': 0,
        't': 0
    }
    count = 0

    for i in range(len(ants)):
        x = ants[i]
        if x in dict:
            dict[x] += 1
        if i > 1:
            if ants[i - 2] == 'a' and ants[i - 1] == 'n' and ants[i] == 't':
                count += 1
    maxi = 0
    for y in dict:
        maxi = dict[y] if dict[y] > maxi else maxi
    return maxi - count


"""
user = User()
user.rank # => -8
user.progress # => 0
user.inc_progress(-7)
user.progress # => 10
user.inc_progress(-5) # will add 90 progress
user.progress # => 0 # progress is now zero
user.rank # => -7 # rank was upgraded to -7
"""

aa = [x for x in range(-8, 9) if x != 0]
print(aa)
ass = 10 * (8 - 3) ** 2
print(ass)


class User:
    rankings = [x for x in range(-8, 9) if x != 0]

    def __init__(self):
        self.rank = -8
        self.rank_ind = 0
        self.progress = 0

    def inc_progress(self, rang):
        difference = 0 if rang * self.rank > 0 else 1
        val = self.rank - rang - difference

        if rang not in self.rankings:
            raise Exception
        elif val > 1 or self.rank == 8:
            return

        if val == 0:
            self.progress += 3
        elif val == 1:
            self.progress += 1
        elif val < 0:
            self.progress += 10 * (rang - self.rank - difference) ** 2
        if self.progress >= 100:
            self.rank_ind += self.progress // 100
            self.progress = self.progress % 100
            if self.rank_ind < 16:
                self.rank = self.rankings[self.rank_ind]
            else:
                self.rank = 8
        if self.rank == 8:
            self.progress = 0


arr = [1,2,3,4]
print(arr[1:1 + 1])


def check(a, s):
    length = len(str(int(a) + 1))
    arr = [a]
    i = len(a)
    while i < len(s):
        if int(s[i: i + length]) == int(arr[-1]) + 1:
            arr.append(s[i: i + length])
            i += length
            length = length + 1 if len(str(int(arr[-1]) + 1)) > length else length
        else:
            return False
    return True


def find(s):
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if check(s[0: j], s):
                return int(s[0: j])
    return int(s)









