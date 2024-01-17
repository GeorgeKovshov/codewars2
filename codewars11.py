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

