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
