arr = [
    [1,2,3,4,5],
    [2,3,4,5,6],
    [9,8,7,6,5],
    [5,2,3,5]
]

for a in arr:
    del(a[a.index(5)])

print(arr)


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

arr = [1, 2, 23, 4, 5, 9]
a = arr[:1] + arr[1:5][::-1] + arr[5:]
print(arr)
print(a)
for i in range(22, 28):
    print(i)

arr = [x if x % 2 == 0 else 0 for x in arr]
print(arr)

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

print(reverse_in_parentheses("many (parens) on (pot)"))